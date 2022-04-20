# Portfolio Project 3 - Data Centric Backend Development

## Online Cookbook - Live Site

[View Live Site](http://flask-cookbook-project-3.herokuapp.com/)

## Business Objectives

As someone who thoroughly enjoys cooking but often struggles to relocate favourite recipes, I have designed and created a website that allows users to store all of their favourite recipes in one space. 

The primary focus for this website is to provide a database for the user so that they can store and access their own chosen recipes with just a few clicks. Users will also be able to add and delete recipes as they please.

The application is designed to be responsive to all screen sizes and accessible to all users, so that navigation is easy for everyone, no matter what device is being used. My goal is to achieve this with a visually appealing, interactive UX, which encourages users to:
- store their favourite recipes in an organised manner
- create/update/delete recipes as they choose
- share the website with friends and family to encourage them to sign up
- follow the company's social media platforms to see other users' recipes and ideas

## Homepage Mockup

![Mock Up Imagery](/static/images/mockup.jpg)

## User Experience (UX)
### User Stories
**First Time Visitor Goals**

1. As a first time visitor, I want to understand what the site's purpose is so that I know whether or not I want to explore further.

2. As a first time visitor, I want to be able to easily register so I can access the rest of the site.

**Returning Visitor Goals**

3. As a returning user, I want to upload my favourite recipes and store them so they are easily accessible for another time.

4. As a returning user, I want to manage my recipes by creating, updating and deleting them when necessary.

**Frequent Visitor Goals**

5. As a frequent user, I want to be able to follow the company's social media platforms so that I can follow them and share my own recipes with them.

6. As a frequent user, I want to be able to store a large variety of recipes in separate categories, in an organised manner, that are easy to locate when I need them.

**Site Owner Goals**

7. As a site owner, I need to enforce some basic access control when a user is editing or deleting data in order to prevent unauthorised editing or deletion of user uploaded data.

## Design
### Colour Scheme
Colour contrast checks were made throughout the process of building the project to save going back and re-doing colours that did not work together.

The main colour scheme is clean and crisp, using different shades of *blue-grey* and *white*, in order to keep the site neutral. The look and feel I wanted to go for was the same look you want to go for with a clean kitchen. People feel most inspired to cook a nice meal when they have a fresh, clean looking kitchen. I wanted that same inspiration throughout the site, and that encourages users to keep their recipes organised.

There are some photographic images throughout, to tie in well with the theme of the site. These images are used on the landing page, and the recipe and category cards.

![Recipe Cards](documentation/images/features/photo.jpg)

The text throughout the site is either white against the blue-grey background, or a dark grey/black against a white background, in order to keep the clean, crisp look throughout the site.

### Typography

Fonts are imported into the CSS file via [Google Fonts.](https://fonts.google.com/)

To keep up with the clean and neutral look of the site, I chose to use just one font that is easy and simple to read.
I have chosen to use the font family of 'Montserrat', with a fallback font of 'san-serif', in the event of the preferred font failing to import. This font will hopefully create a positive user experience when first entering the site as it exudes a professional yet simplistic mood.

![Monseratt font](documentation/images/features/font.jpg)

### Imagery

Photographic imagery is used in some parts of the site, all images are sourced from [Pixabay.](https://pixabay.com/photos/search/)

The landing page consists of a header, background image and a footer. The image has been slightly darkened and the opacity reduced so that it wasn't too vibrant against the subtle colours of the header and footer.

This image gives the user a good idea of what the site is about upon entering. The appealing image of fresh food should give the user motivation to explore the site further.

The Recipes page that contains all of the users' recipes consists of 4 diet specific categories. Each category has a card element containing an image related to that category, e.g. an image of a vegetable curry for the vegetable category.

The Manage Categories page consists of 4 images for each category, these images are the same for each category for ease which I may change at a later date.

![Various Imagery](/documentation/images/features/imagery.jpg)

***Since writing up the Imagery documentation, I decided to change the background image used on the Landing Page. This was purely down to personal preference and I do think the darker image works better against the white text. See new Landing Page below.***

![New Landing Page Imagery](/static/images/newlanding.jpg)

## Wireframes
Wireframes for the original design concepts across all devices were created using [Balsamiq.](https://balsamiq.com/wireframes/)

**Home Page**

The landing page explains the purpose of the site to new and returning users through imagery and subheadings. Functionality is limited from this page as users are only able to register, log-in or visit the company's social media platforms.

![Home Page Wireframe](/documentation/images/wireframe-imgs/landingpage.jpg)

**Register Page**

Register page enables the user to create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries and password confirmation.

![Register Page Wireframe](/documentation/images/wireframe-imgs/register.jpg)

**Log-in Page**

For returning users there is a log-in page to enable access to the full functionality of the site.

![Log-in Page Wireframe](/documentation/images/wireframe-imgs/login.jpg)

**Profile Page**

Upon successful registration or logging in, users are directed to their profile page, consisting of a welcome message that contains the session users' username.

![Profile Page Wireframe](/documentation/images/wireframe-imgs/profile.jpg)

**Recipe Page**

The Recipe page is the main attraction/functionality of the site. By retrieving the data from the Mongo database, recipes are displayed by category for the user to access. Users are also able to search and filter recipes by entering a recipe name or diet category.

![Recipes Page Wireframe](/documentation/images/wireframe-imgs/myrecipes.jpg)

**Add Recipe Page**

Users can add a recipe by filling out the following input fields:

- Recipe Name
- Veggie Safe (on/off switch)
- Diet Category
- Cooking Time
- Cooking Skill Level
- Serves (how many)
- Ingredients
- Method

![Add a Recipe Page Wireframe](/documentation/images/wireframe-imgs/addrecipe.jpg)

**Edit Recipe Page**

Each recipe has a edit & delete button. By clicking the *edit* button, users are directed to the Edit Recipe page, where all fields hold the value of the already submitted recipe. Users can change the input text as necessary and update to the database.

![Edit a Recipe Page Wireframe](/documentation/images/wireframe-imgs/editrecipe.jpg)

**Manage Categories Page**

This page is restricted to the admin only, where they can choose to create, update or delete diet categories.

![Manage Categories Page Wireframe](/documentation/images/wireframe-imgs/managecategories.jpg)

**Add Category Page**

After clicking the *Add Category* button on the previous page, users can populate the input field with a new category.

![Add Categories Page Wireframe](/documentation/images/wireframe-imgs/addcategory.jpg)

**Edit Diet Category Page**

After clicking the *Edit* button on a specific category card, users can populate the input field with the updated category.

![Edit Category Page Wireframe](/documentation/images/wireframe-imgs/editcategory.jpg)

## Database schema

I used Mongo DB Atlas, a non-relational database to store and retrieve all of the user input data, illustrated below:

![Database](/documentation/images/features/data.jpg)

- The *Users* collection stores user data, including a usernsame and password that they will input each time they are required to log in. The username is used to populate the *created by* field in the *Recipes* collection when a user uploads a new recipe.

- The *Recipes* collection is the largest in the database and stores all user input regarding each recipe, as well as data retrieved from other collections. I included all elements of a recipe that I thought were most relevant for each field.

- The *Categories* collection consists of user input regarding the diet type of that recipe. Which is then injected into the *Recipes* collection as the *diet_name*.

## Features
### Existing Features
| Feature | Description | Image URL |
| ------- | ----------- | --------- |
| Landing | Landing page to convey the purpose of the website to new and returning users. | |
| Header | Logo and nav bar allow user to navigate through the site with ease. Burger icon displays on smaller devices. | [Header](/documentation/images/features/header.jpg) |
| Footer | Sign up option and social media icons direct the user to the company's social media platforms. | [Footer](/documentation/images/features/footer.jpg) |
| Register | Provides the opportunity for new users to sign-up quickly and efficiently. | [Registration Page](/documentation/images/features/register.jpg) |
| Log-In | Provides the opportunity for returning users to log-in quickly. | [Log-In Page](/documentation/images/features/log-in.jpg) |
| Profile Page | Users are directed to a welcome message displaying their username. | [Profile Page](/documentation/images/features/profile.jpg) |
| Recipes | Page where all users' recipes are displayed. | [Recipes Page](/documentation/images/features/recipes.jpg) |
| Recipe Search | Users can text search for a recipe using the recipe name or diet category. | [Recipe Search](/documentation/images/features/recipe-search.jpg) |
| Drop Down Recipes | Recipes are organised with dropdown select elements. Users select/drop the recipe they want to view. | [Dropdown Recipe](/documentation/images/features/dropdown.jpg) |
| Add Recipe | Users can create and upload a recipe to their database. | [Add Recipe](/documentation/images/features/add-recipe.jpg) |
| Edit Recipe | Enables users to modify all of the fields for any of the recipes they uploaded. Original data is uploaded from the database into the value fields until the user modifies. | [Edit Recipe](/documentation/images/features/edit-recipe.jpg) |
| Delete Recipe | Allows user to delete a recipe that they have uploaded. | [Delete Recipe](/documentation/images/features/delete.jpg) |
| Manage Categories | Admin access only. Admin has the ability to create, update or delete diet categories. | [Manage Categories Page](/documentation/images/features/manage-cat.jpg) |
| Log-Out | Logs user out and clears session | [Log Out](/documentation/images/features/logout.jpg) |

### Security Features

Although certain security features were not required for this project I have chosen to implement basic measures to provide some protection against unauthorised access to other users data.

| Feature | Description | Image URL |
| ------- | ----------- | --------- |
| User Log-In | A simple username and password is required for registration. Password gets hashed using Password Hash from the Werkzeug Library. | [Log-In Security](/documentation/images/features/login-security.jpg) |
| Session Cookie | Upon registering or logging in, a unique session cookie is generated for the duration of the users' session. Recipe uploads are saved in the database against the session cookie username. | [Session Cookie](/documentation/images/features/session.jpg) |
| Restricted Access | Users cannot edit or delete recipes that are not uploaded by them. Only admin users can manage categories. In the Image URL, you can see that only the username of *laurajones* will be able to edit or delete the recipe. | [Restricted Access](/documentation/images/features/access.jpg) | 
| Password Confirmation | When registering, a password confirmation input field is displayed to ensure the user signing up is genuine. | [Password Confirmation](/documentation/images/features/password-conf.jpg) |



### Features yet to implement

| Feature | Description |
| ------- | ----------- |
| Dropdown for all Recipes | At the moment, all recipe names are visible under their category, ready to be selected and dropped down for full visibility. For better organisation, I would like to hide all recipes until the user clicks a drop down button (on the chosen category card) that will reveal all recipes under that category. |
| Next/Previous button | Incase the *My Recipes* page becomes too crowded once a user has uploaded a lot of recipes, I would like to set a limited amount of recipes that are shown below the category cards, and when that number of recipes is exceeded there is a *next* button that allows the user to skip to the next lot of recipes. |
| Family accounts | Once I have built up the knowledge required to be able to take the web app further, I would like to provide the opportunity to hold family/household accounts where users of the same family can log into the same account but have their own individual profile that only they can manage. |
| Profile Management | I would like to add a management system for users to be able edit their profiles and populate elements such as, usernames, profile picture, favourite recipe/food. |
| Delete confirmation | On developing the website further I would like to add a modal that appears when a user attempts to delete a recipe or category. The modal will ask the user if they are sure that they want to delete, to prevent any accidental deletions.

## Technologies Used
### Languages
- HTML5
- CSS3
- Python
- JavaScript


### Libraries/Integrations

- Flask - Flask micro-framework, links with jinja to create the webpages.

- Jinja - The project uses the Jinja templating engine.

- Materialize CSS - Grid system as well as other elements used throughout the site.

- Hover.css - Used in the Footer to highlight when links are hovered over.

- Google Fonts - Imported via CSS.

- Font Awesome - Icons used for social media links as well.

- Balsamiq - Used to create wireframes for the project.

### Database Management System

- MongoDB Atlas

### Version Control, Storage & Hosting

- Chrome Dev Tools - Heavily used to fix any spacing issues as well as testing responsivity.

- Github - To store repositories and codes after being pushed on Gitpod.

- Git - Used for version control and tracking changes made to files.

- Gitpod - Used for the workspace for this project.

- Heroku - Deployment site.

- Multi Device Mockup Generator (techsini) - To create an image of what the project will look like on various devices. [TechSini.com](http://techsini.com/multi-mockup/index.php)

- WebAIM Contrast Checker - To test colours throughout the site for whether or not they will produce good user experience.

- W3C Markup Validator - Checks HTML code for errors and warnings.

- W3C CSS Validator - Checks CSS code for errors and warnings.

- JShint - Checks JavaScript code for errors and warnings.

- PEP8 Validator - Checks that the Python code is PEP8 compliant.

## Testing

All testing for this project can be found in the [TESTING.md file](TESTING.md).

## Creating the Database

The key features required for this app to function as designed are centred around CRUD interactions with a MongoDB Atlas cloud database management system:

- Create or upload a recipe into the database which can then be viewed by all other registered users.
- Read or view all of the recipes stored in the database.
- The list of recipes can be searched by recipe name or category name.
- Update any of their own recipes, to change any of the previously stored content, or add additional information.
- Delete recipes they themselves have uploaded. This provides restricted access.

This app is connected to a MongoDB Atlas Cluster. The following steps were used to create the MongoDB Project Database:

1. Register/log-in to MongoDB Atlas.
2. Create a new project.
3. Click 'Build a Database'.
4. Locate the free, 'Shared' database and click 'Create'.
5. Ensure that you have the 'AWS' Cloud Provider selected, and that you have selected the region closest to you. Ensure that the Cluster Tier is of M0 Sandbox, then click 'Create Cluster'. *See below*.

![Create Database](/documentation/images/testing/createdb.jpg)

6. Create your username and password and ensure that 'My Local Environment' is selected for the network connection.
7. Add IP Address and allow Access from Anywhere (Not recommended for full production apps).
8. Once the database is active, you can connect it to Git or whatever version control you are working from.
9. Click Collections to add a database and start adding documents to your database collections by providing a database name and adding a name for your first collection of documents.

## Deployment

This project was created using Gitpod, which enabled me to stage and commit the files via Git (version control). ll of the files necessary to run this website have been stored in a GitHub repository.

### Forking the GitHub repository

1. Select the repository you wish to fork.
2. In the top right corner of the page (under your account icon) there will be an option to Fork.
3. By selecting Fork you will now have a copy of the respository in your own Github account.

### Cloning the Github Repository:

1. Select the repository you wish to clone locally.
2. Above the files, locate the Code dropdown menu.
3. Select and copy the link appropriately (HTTPS, SSH, Github CLI).
4. Open the terminal and change the directory to where you want the cloned version to be located.
5. Type git clone and paste the copied link.
6. Press Enter to create local clone.

### Creating the Heroku App

As this is a full-stack website it has been deployed to Heroku.com using the following procedure:

1. Register/log-in to Heroku.
2. From the Dashboard, select the "New" button on the top-Right of the screen, then select "Create new app".
3. Choose your app name.
4. Select your region.
5. Click "Create App".

### Heroku Deployment

1. In the "Deployment Method" section, select Github. Locate the Connect to GitHub section below.
2. Your Github profile should be displayed, if not type in your GitHub username.
3. Select the corresponding repository, and click "Connect".

Configuration settings and secret keys are needed for this app, which Heroku requires in order for the website to function as desired. To do this you need to set the Config Vars within Heroku:

5. Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.
6. This will reveal a form for inputting the key and value pairs necessary to connect to the app, as follows:

| KEY | VALUE |
| --- | ----- |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET KEY | Randomly Generated Fort Knox Key |
| MONGO_URI | Your unique MongoDB URI |
| MONGO_DBNAME | Your unique Mongo DB name |

You can find the above Mongo_URI value in the appropriate Mongo DB Project under Cluster by selecting "Connect".

7. Select "Clusters".
8. Select "Connect".
9. Select "Connect your application".
10. Choose your Driver and Version.
11. Copy your connection string.

***Remember to substitute in your own DBNAME and Password***

### Enabling Automatic Deployment

1. In Heroku, click the "Deploy" tab.
2. In the "Automatic deploys" section select the branch you wish to use.

***Since first deploying the application on Heroku, Heroku themselves have encountered a security problem and therefore have had to remove certain functionalities that would allow users to automatically deploy or update. All deployments are now carried out manually using the following procudure:***

1. In the terminal, run the command `heroku login -i` and login when prompted.
2. Run the following command: `heroku git:remote -a your_app_name_here` and replace `your_app_name_here` with the name of your Heroku app. This will link the app to your Gitpod terminal, and the Heroku app to the Gitpod workspace.
3. After linking your app to your workspace with one of the above steps, you can then deploy new versions of the app by running the command `git push heroku main` and the app will be deployed to Heroku.

## Credits
Code
Stackoverflow Forums

As stated in the comments of the CSS file (lines 4-5), for providing a solution to fix an issue regarding white space down the right side of the page.
Brian, Program Director, Code Institute

For giving me the idea to have the navbar on the right side of the header (custom CCS used).
Matt Rudge, Code Institute

For providing me the idea to use a hover effect on icons. I used this effect on the contact icon and social media icons (custom CSS styling was used).
The idea for the style and layout for the contact form was inspired by the Love Running Project. Again, I used custom CSS styling.
Maggie Walsh (fellow Stack member)

For sharing advice with members regarding the basic structure of a README.md file.
Media
Jess Hynes (client)
Providing the photographic images to use as hero images.
Providing permission to use YouTube links to videos that she has recorded and uploaded from her home studio.
Acknowledgements
Code Institue Tutors

For showing me guidance when using the display attribute to align content in rows and columns, so that it is spaced evenly across the page.
Felipe Souza Alarcon, my Code Institute mentor throughout the course

For continous support and professional guidance during the process of building my project.
Fellow Slack Community members

For responding when in times of need.

## Personal Development
Following a session with my Code Institute mentor, I have noted that for future projects I will pay extra attention to how I am writing up CSS code, so that I don't end up with repetitive, unnecessary lines of code. In the meantime I am going to research different methods and ways of creating effective code that does not use a large amount of lines within the CSS file.

After writing my Personal Development section I decided to go back into my CSS file and attempt to slim down on the amount of code being used. I was able to remove approx. 200 lines of code by testing with Chrome Dev Tools and removing any unnecessary or repetitive code.