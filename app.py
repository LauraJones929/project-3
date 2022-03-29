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


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


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
    return render_template("register.html")


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
                    flash("Hello, {}! You have successfully logged in!".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Uh oh! You have entered an incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Uh oh! You have entered an incorrect Username and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
