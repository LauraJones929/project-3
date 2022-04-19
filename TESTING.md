# Testing

Most testing was carried out via Google Chrome browser and Chrome Dev Tools for responsivity and checking to see if the JavaScript/Python code was working as expected, throughout the process of building the project. Microsoft Edge and Firefox was also used for testing overall performance and responsivity. I also tested the site on an iPhone 12 for responsivity, this included Google Chrome and Safari browsers.

## User Story Testing

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 1 | "As a first time visitor, I want to understand what the site's purpose is so that I know whether or not I want to explore further." | Upon entering the site, the user is directed straight to the landing page where a clear explanation of the app's purpose with both text and imagery. |

![Landing Page](/documentation/images/testing/landing.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 2 | "As a first time visitor, I want to be able to easily register so I can access the rest of the site." | Registration is quick and simple, requiring the user to provide a valid username, email-address and password. |

![Registration](/documentation/images/testing/register.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 3 | "As a returning user, I want to upload my favourite recipes and store them so they are easily accessible for another time." | Registered users are able to create, upload and store their recipes in an organised manner. A search bar is displayed at the top of the *Recipes* page for a quick way to find a specific recipe. |

![Add a recipe](/documentation/images/testing/add-recipe.jpg)

![A recipe](/documentation/images/testing/dropdown.jpg)

![Search bar](/documentation/images/testing/search.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 4 | "As a returning user, I want to manage my recipes by creating, updating and deleting them when necessary." | Once a recipe has been created, users are able to edit and delete a recipe as they wish. |

![Edit or Delete a Recipe](/documentation/images/testing/access.jpg)

![Edit a recipe](/documentation/images/testing/edit-recipe.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 5 | "As a frequent user, I want to be able to follow the company's social media platforms so that I can follow them and share my own recipes with them." | Social Media icons provide a link to the company's social media platform. These are visible at all times in the Footer. |

![Social Media links](/documentation/images/testing/footer.jpg)

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 6 | "As a frequent user, I want to be able to store a large variety of recipes in separate categories, in an organised manner, that are easy to locate when I need them." | When uploading a recipe to the database, the user must select what diet category their recipe belongs to. This will then store that recipe in the correct category showing on the site. Categories are also searchable in the Search bar. |

![Vegetarian & Vegan Categories](/documentation/images/testing/veggievegan.jpg)

![Meat & Pesce Categories](/documentation/images/testing/recipes.jpg)

![Search Pescetarian](/documentation/images/testing/searchcategory.jpg)

![Pescetarian Recipes](/documentation/images/testing/searchcategory2.jpg)

*When the category name 'Pescetarian' was searched, only the recipes in the Pescetarian category was shown.*

| User Story | Description | Testing |
| ------- | ----------- | --------- |
| 7 | "As a site owner, I need to enforce some basic access control when a user is editing or deleting data in order to prevent unauthorised editing or deletion of user uploaded data." | Users can only *edit* or *delete* a recipe that they themselves have uploaded. |

![No access to edit](/documentation/images/testing/noaccess.jpg)

*The edit and delete button does not show.*

## Functionality Testing

The following tables show the functionalality testing performed on the web-app to ensure it works as desired. I have tested on a Windows device on the listed browsers.

### Navigation Testing

Tests the navbar selections and various anchor links provided to assist users navigating between pages.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 001 | Home link on navbar | Directs user to homepage | Opens homepage | PASS | PASS | PASS |
| 002 | Brand logo | Directs user to homepage | Opens homepage | PASS | PASS | PASS |
| 003 | Home link on mobile nav | Directs user to homepage | Opens homepage | PASS | PASS | PASS |
| 004 | Log-in link on navbar | Directs user to log-in page | Opens log-in page | PASS | PASS | PASS |
| 005 | Log-in link on mobile nav | Directs user to log-in page | Opens log-in page | PASS | PASS | PASS |
| 006 | Log-in redirect link on registration page | Directs user to log-in page | Opens log-in page | PASS | PASS | PASS |
| 007 | Registration link on navbar | Directs user to registration page | Opens registration page | PASS | PASS | PASS |
| 008 | Registration link on mobile nav | Directs user to registration page | Opens registration page | PASS | PASS | PASS |
| 009 | Registration redirect link on log-in page | Directs user to registration page | Opens registration page | PASS | PASS | PASS |
| 010 | Sign-up/registration link in footer | Directs user to registration page | Opens registration page | PASS | PASS | PASS |

### Registration/Log-In Testing

Testing the registration process for new users and the log-in process for returning users. The app should provide feedback to the user in cases where incorrect inputs are provided.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 011 | Username input | Feedback when requirements not met | Input box turns red and tooltip provides feedback | PASS | PASS | PASS |
| 012 | Password input | Feedback when requirements not met | Input box turns red and tooltip provides feedback | PASS | PASS | PASS |
| 013 | Password confirmation | Feedback when passwords do not match | Confirm Password input field remains red until passwords match. Turns green on matching | PASS | PASS | PASS |
| 014 | Username already exists | Let user know the username is not available | Flash message letting user know the username already exists. | PASS | PASS | PASS |
| 015 | Password confirmation | Feedback when passwords do not match | Confirm Password input field remains red until passwords match. Turns green on matching | PASS | PASS | PASS |
| 016 | Incorrect username | Inform user of a incorrect username OR password | Flash message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |
| 017 | Incorrect password | Inform user of a incorrect username OR password | Flash message letting user know that either an incorrect username or password has been entered | PASS | PASS | PASS |

![Incorrect Username/Password](/documentation/images/testing/incorrect.jpg)

![Requirements not met](/documentation/images/testing/characters.jpg)

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 018 | Registration successful | User directed to Profile page with welcome message displayed | Profile page is loaded, displaying welcome message that includes the users' chosen username | PASS | PASS | PASS |
| 019 | Log-In successful | User directed to Profile page with welcome message displayed | Profile page is loaded, displaying welcome message that includes the users' chosen username | PASS | PASS | PASS |

![Profile Page](/documentation/images/testing/profile.jpg)

### Recipe Search & View (READ)

Testing the ability to view the recipe collection, filter by diet category or recipe name and perform a text search. Clicking the name of each recipe should also reveal the full recipe details.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 020 | Navigate to Recipes page (navbar) | Direct user to Recipes Page | Recipes page is loaded | PASS | PASS | PASS |
| 021 | Navigate to Recipes page (mob nav) | Direct user to Recipes Page | Recipes page is loaded | PASS | PASS | PASS |
| 022 | Categories and recipes organised & displayed | Recipes are organised by diet category | Recipes are visible beneath their category, waiting to be selected | PASS | PASS | PASS |
| 023 | Recipe selected (dropdown) | Full recipe shown when user selects and clicks on the element | Recipe successfully drops down to show full details when clicked | PASS | PASS | PASS |
| 024 | Recipe search | Show results based on user input | Correctly returns recipes and only shows matching results | PASS | PASS | PASS |

### Add Recipe (CREATE)

Testing the ability to upload a new recipe to the database collection.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 025 | Navbar link | Direct user to Add a Recipe Page | Add a Recipe page is loaded | PASS | PASS | PASS |
| 026 | Mob nav link | Direct user to Add a Recipe Page | Add a Recipe page is loaded | PASS | PASS | PASS |
| 027 | Recipe Name | User can input name of recipe as desired | Recipe name successfully inserted. Feedback provided if character count is less than 5 | PASS | PASS | PASS |
| 028 | Vegetarian switch | Marks recipe as 'veggie-safe' or not | When switched 'on', the recipe is marked as 'veggie-safe' at the front-end | PASS | PASS | PASS |
| 029 | Cooking Time | Displays cooking time | User can input the cooking time. Feedback provided if character count is less than 2 | PASS | PASS | PASS |
| 030 | Skill Level | Displays skill level | User can input the skill level of the recipe. Feedback provided if character count is less than 3 | PASS | PASS | PASS |
| 031 | Serves | Displays how many people can be served | User can input the number of people can be served. Feedback provided if character count is less than 5 or if any characters have been used other than 0-9 | PASS | PASS | PASS |
| 032 | Ingredients | Displays ingredients needed | User can input the ingredients needed in the text area. Feedback provided if character count is less than 10 | PASS | PASS | PASS |
| 033 | Method | Displays recipe method | User can input the recipe method in the text area. Feedback provided if character count is less than 10 | PASS | PASS | PASS |
| 034 | Add a Recipe button | Uploads recipe and redirects user to the My Recipes page | User can successfully upload a recipe and is redirected to My Recipes page. Flash message states recipe was successfully added. | PASS | PASS | PASS |
| 035 | Data Written to MongoDB | Confirm new recipe data is written to MongoDB | New recipes appear in the Recipes collection within Mongo DB. All fields are populated if completed | PASS | PASS | PASS |
| 036 | Added to Recipes page | New recipe successfully renders on My Recipes page | The new recipe renders as intended on the My Recipes page | PASS | PASS | PASS |

### Edit Recipe (UPDATE)

Testing the ability to retrieve a previously uploaded recipe from the database and edit any of the data previously supplied.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 037 | Edit button | Direct user to Edit Recipe Page | Edit Recipe page is loaded | PASS | PASS | PASS |
| 038 | Restricted Access | Users can only edit their own recipe | Edit button displays only for the user that it was created by | PASS | PASS | PASS |
| 039 | Existing data renders | Display existing recipe data from the database onto the form | All of the existing data is loaded into the form fields | PASS | PASS | PASS |
| 040 | Edit button | Direct user to Edit Recipe Page | Edit Recipe page is loaded | PASS | PASS | PASS |
| 041 | Recipe Name | Recipe name can be edited | User can edit and delete the recipe name | PASS | PASS | PASS |
| 042 | Vegetarian switch | Switch can be changed | User can toggle the switch from on/off | PASS | PASS | PASS |
| 043 | Cooking Time | Text can be edited | User can edit and delete the cooking time. | PASS | PASS | PASS |
| 044 | Skill Level | Text can be edited | User can edit and delete the skill level | PASS | PASS | PASS |
| 045 | Serves | Text can be edited | User can edit and delete the number of people served | PASS | PASS | PASS |
| 046 | Ingredients | Text can be edited | User can edit and delete the ingredients needed in the text area | PASS | PASS | PASS |
| 047 | Method | Text can be edited | User can edit and delete the method in the text area | PASS | PASS | PASS |
| 048 | Edit Recipe button | Saves and uploads edited recipe to the database and redirects user to the My Recipes page | User can successfully edit a recipe and is redirected to My Recipes page. Flash message states recipe was successfully edited | PASS | PASS | PASS |
| 049 | Data Written to MongoDB | Confirm recipe data is edited and written to MongoDB | Edited recipes appear in the Recipes collection within Mongo DB. All fields are populated if completed | PASS | PASS | PASS |
| 050 | My Recipes updated | Edited recipe successfully renders on My Recipes page | The edited recipe renders as intended on the My Recipes page | PASS | PASS | PASS |

### Delete Recipe (DELETE)

Testing for successful deletion of the recipe from the web-app and from the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 051 | Edit button | Direct user to Edit Recipe Page | Edit Recipe page is loaded | PASS | PASS | PASS |