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

## Functionality Testing (Manual)

The following tables show the functionality testing performed on the web-app to ensure it works as desired. I have tested on a Windows device on the listed browsers.

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

### Manage Categories

Testing the ability to create, edit and delete the diet categories from the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 051 | Navbar link (restricted access) | Directs user (admin) to Manage Categories page | User (admin) is successfully directed to the Manage Categories page | PASS | PASS | PASS |
| 052 | Admin-only access | Manage Categories page is only accessible by the admin | Username 'admin123' can access the Manage Categories page. Other usernames cannot. | PASS | PASS | PASS |
| 053 | Categories displayed | Existing diet categories within the database are displayed in card elements | User (admin) is able to view the category cards, with the options to edit or delete | PASS | PASS | PASS |
| 054 | Edit Button | Directs admin to Edit Category page where the name of the category can be changed | Admin is successfully directed to the Edit Category page and is able to edit the name of the category. Category name is successfully updated in the database | PASS | PASS | PASS |
| 055 | Delete Button | Deletes category | User can successfully delete a category from the web app and the database | PASS | PASS | PASS |
| 056 | Add a Category | Creates a new category | Admin is able to create a new category that will be visible to all users | PASS | PASS | PASS |

### Delete Recipe (DELETE)

Testing for successful deletion of the recipe from the web-app and from the database.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 057 | Delete button | Recipe is deleted from database | User can successfully delete recipe from the app and database | PASS | PASS | PASS |
| 058 | Restricted Access | Users can only delete their own recipe | Delete button displays only for the user that it was created by | PASS | PASS | PASS |

### Other Links

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 059 | Social Media Links | Social Media icons to perform as a link that directs user to the company's social media platforms | User is directed to the social media platform when relevant icon is clicked | PASS | PASS | PASS |

## Appearance Testing

The following tables show the appearance testing to check for any differences across different web browsers. This web app was developed on a Google Chrome browser, on a Windows Laptop. The app has also been regularly tested on Firefox and Microsoft Edge.

| Page | Google Chrome | Edge | Firefox |
| ---- | ------------- | ---- | ------- |
| Landing Page | No visible difference | No visible difference | h1 heading is less bold |
| Registration Page | No visible difference | No visible difference | No visible difference |
| Log-In Page | No visible difference | No visible difference | No visible difference |
| Profile Page | No visible difference | No visible difference | No visible difference |
| My Recipes Page | No visible difference | No visible difference | Placeholder text is lighter than other browsers. Recipes text is bolder
| Add a Recipe Page | No visible difference | No visible difference | No visible difference |
| Edit Recipe Page | No visible difference | No visible difference | Input text appears to be darker/bolder but less sharp
| Manage Categories Page | No visible difference | No visible difference | No visible difference |
| Edit Category Page | No visible difference | No visible difference | No visible difference |
| Add Category Page | No visible difference | No visible difference | No visible difference |

## Code Quality and Validation

Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results for these tests are shown below.

| Test | Process | Result | Image URL | Comment |
| ---- | ------- | ------ | --------- | ------- |
| HTML Validation | Copy page URI into W3C validator | 1 Warning - Section lacks headers | [HTML W3C Validator Results](/documentation/images/testing/htmlvalid.jpg) | The page has a heading. This is not a conventional website page layout of multiple headed sections |
| CSS Validation | Copy page URI into W3C validator | 7 Warnings - Related to Materialize CSS | [CSS W3C Validator Results](/documentation/images/testing/cssvalid.jpg) | The errors that have shown are related to the Materialize CSS that I have used. Layout or functionality of the app is not affected |
| Python Validation | Copy Python code into PEP8 validator | No issues | [Pep8 Validator Results](/documentation/images/testing/pep8.jpg)
| JavaScript Validation | Copy JavaScript code into JShint | Warnings | [JShint Validator Results](/documentation/images/testing/jshint.jpg) | Warning related to Materialize CSS code and ES6 versions. Web app not affected |

## Responsivity Testing

I have carried out continuous responsiveness testing, throughout building the project, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools. The website was built and tested on a Windows 11 Lenovo Laptop. Other devices that the website has been tested on:

- Attached Dell monitor
- iPhone 12

![Mobile Responsivity](/documentation/images/testing/responsive1.jpg)

![Tablet Responsivity](/documentation/images/testing/responsive2.jpg)

![Mobile Responsivity](/documentation/images/testing/responsive3.jpg)

## Performance Testing

Further testing using the following tools:

- Google Lighthouse (Desktop)

![Performance Testing](/documentation/images/testing/performance.jpg)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 89% | 94% | 83% | 89% |
| Registration Page | 100% | 93% | 83% | 89% |
| Log-In Page | 100% | 93% | 83% | 89% |
| Profile Page | 100% | 90% | 83% | 89% |
| My Recipes Page | 95% | 85% | 83% | 80% |
| Add a Recipe Page | 100% | 84% | 83% | 89% |
| Edit Recipe Page | 100% | 84% | 83% | 89% |
| Manage Categories Page | 96% | 80% | 83% | 80% |
| Add a Category Page | 100% | 93% | 83% | 89% |
| Edit Category Page | 100% | 93% | 83% | 89% |

- Google Lighthouse (Mobile)

| Page | Performance | Accessibility | Best Practices | SEO |
| ---- | ----------- | ------------- | -------------- | --- |
| Landing Page | 73% | 90% | 83% | 91% |
| Registration Page | 97% | 93% | 83% | 91% |
| Log-In Page | 98% | 93% | 83% | 91% |
| Profile Page | 97% | 90% | 83% | 91% |
| My Recipes Page | 78% | 85% | 83% | 83% |
| Add a Recipe Page | 96% | 84% | 83% | 89% |
| Edit Recipe Page | 96% | 84% | 83% | 89% |
| Manage Categories Page | 73% | 80% | 80% | 83% |
| Add a Category Page | 97% | 93% | 83% | 91% |
| Edit Category Page | 96% | 93% | 83% | 91% |

## Security Testing

Testing security measures that are in place to improve user experience and confidentiality.

| Test | Element | Desired Result | Actual Result | Google Chrome v 100.0.4896.88 | Edge v 100.0.1185.44 | Firefox v 99.0.1 (64-bit) |
| ---- | ------- | -------------- | ------------- | ---------- | --------------- | ---------- |
| 060 | Username Duplication | No username duplication allowed | Registration will check for username duplication. A flash message will warn the user if the username already exists | PASS | PASS | PASS |
| 061 | Password security | Password is hashed | The password is converted into a complicated string or an algorithm | PASS | PASS | PASS |
| 062 | Password confirmation | Checks for password match | When the password confirmation input matches the first password input, feedback validation is given and the user can register successfully | PASS | PASS | PASS |
| 063 | Restricted access | Users are only able to edit or delete their own recipe | The *edit* and *delete* buttons are only visible to the user who created the recipe | PASS | PASS | PASS |
| 064 | Admin access | Only the admin user can edit or delete categories | The *Manage Categories* link in the navbar is only visible to admin users | PASS | PASS | PASS |

## Additional Testing

I used the a11y Contrast Checker to test all colours throughout the project. As you can see there has been some problems detected regarding the grey/white contrast that runs throughout the website, as well as the pink/white that I used for the *Reset/Cancel* buttons. I am happy to leave these colours as they are as I want to create a soft, subtle look to the entire site. By changing this soft tone to something more contrasting and vibrant, I fear that the intended look will be lost. After further testing on different screens, I can confidently say that the grey text is easily read-able, and the buttons are highly visible, and are not at all lost in the  white background.

![Colour Contrast Checker](/documentation/images/testing/colour-contrast.jpg)

# Known Bugs & Fixes

| Issue # | Bug | Description | Solution |
| ------- | --- | ----------- | -------- |
| 1 | White-space in text areas | When clicking on the text area for the *Ingredients* and *Method* I noticed there was some white space, which affected the validation feedback when filling in the form. | I remembered seeing this on the Code Institute tutorials as this was an issue that came up during a walkthrough project. I was able to follow this advice and get rid of the whitespace by using the closing tag `</textarea>` on the same line of the last line of text.
| 2 | White-space on either side of Landing Page image (desktop only) | When viewing the web-app on a desktop, you can see there is a fair amount of white-space on either side of the image, as opposed to stretching across the entire screen. | No solution yet - I have researched on various forums and websites how to get rid of the unwanted white-space but have not yet found a solution that works as desired. I could inject the background image into the `<body>` element of the page,which will allow the image to fill the entire screen, however I don't want to use the background image across the entire site, only the landing page. |

[Back to README.md file](README.md)