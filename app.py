import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# renders the landing page template
@app.route("/")
def index():
    return render_template("index.html")


# renders the Recipes page and retrieves data from mongo db
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# allows users to filter documents from the db
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# allows users to register a new account
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # checks db for username availability
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_exists:
            flash("This Username already exists. Please choose another.")
            return redirect(url_for('register'))

        sign_up = {
            "username": request.form.get("username"). lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # insert new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful! You can now log in!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# allows users to log into their account
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks db for username availability
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # checks user input matches hashed password
            if check_password_hash(
                user_exists["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello, {}! You have successfully logged in!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash(
                    "Uh oh! You have entered an incorrect"
                    "Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash(
                "Uh oh! You have entered an incorrect"
                "Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# redirects user to profile template upon logging in successfully
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # fetch session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# allows users to log out
@app.route("/logout")
def logout():
    # removes user from session cookies
    flash("You have successfully logged out!")
    session.clear()
    return redirect(url_for("login"))


# allows users to add new recipe and posts to db
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian-switch") else "off"
        recipe = {
            "diet_name": request.form.get("diet_name"),
            "recipe_name": request.form.get("recipe_name"),
            "vegetarian": vegetarian,
            "cooking_time": request.form.get("cooking_time"),
            "skill_level": request.form.get("skill_level"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("get_recipes"))

    diets = mongo.db.categories.find().sort("diet_name", 1)
    skills = mongo.db.recipes.find().sort("skill_level", 1)
    return render_template("add_recipe.html", diets=diets, skills=skills)


# allows users to edit a recipe and posts to db
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian-switch") else "off"
        edit = {"$set": {
            "diet_name": request.form.get("diet_name"),
            "recipe_name": request.form.get("recipe_name"),
            "vegetarian": vegetarian,
            "cooking_time": request.form.get("cooking_time"),
            "skill_level": request.form.get("skill_level"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }}
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    diets = mongo.db.categories.find().sort("diet_name", 1)
    skills = mongo.db.recipes.find().sort("skill_level", 1)
    return render_template("edit_recipe.html", recipe=recipe,
        diets=diets, skills=skills)


# allows users to delete a recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("get_recipes"))


# renders the categories template
@app.route("/get_categories")
def get_categories():
    diets = list(mongo.db.categories.find().sort("diet_name", 1))
    return render_template("categories.html", diets=diets)


# allows users to add a category and posts to db
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "diet_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Successfully Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# allows users to edit a category and posts to db
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {"$set": {
            "diet_name": request.form.get("category_name")
        }}
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# allows users to delete a catory
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted!")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
