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

## User Experience (UX)
### User Stories
**First Time Visitor Goals**

- As a first time visitor, I want to understand what the site's purpose is so that I know whether or not if I want to explore further.

- As a first time visitor, I want to be able to easily register so I can access the rest of the site.

**Returning Visitor Goals**
- As a returning user, I want to upload my favourite recipes and store them so they are easily accessible for another time.

- As a returning user, I want to manage my recipes by creating, updating and deleting them when necessary.

**Frequent Visitor Goals**
- As a frequent user, I want to be able to follow the company's social media platforms so that I can follow them and share my own recipes with them.

- As a frequent user, I want to be able to store a large variety of recipes in separate categories, in an organised manner, that are easy to locate when I need them.

**Site Owner Goals**
- As a site owner, I need to enforce some basic access control when a user is editing or deleting data in order to prevent unauthorised editing or deletion of user uploaded data.

## Design
### Colour Scheme
Colour contrast checks were made throughout the process of building the project to save going back and re-doing colours that did not work together.

The main colour scheme is clean and crisp, using different shades of *blue-grey* and *white*, in order to keep the site neutral. The look and feel I wanted to go for was the same look you want to go for with a clean kitchen. People feel most inspired to cook a nice meal when they have a fresh, clean looking kitchen. I wanted that same inspiration throughout the site, and that encourages users to keep their recipes organised.

There are some photographic images throughout, to tie in well with the theme of the site. These images are used on the landing page, and the recipe and category cards.

![Recipe Cards](documentation/images/features/photo.jpg)

The text throughout the site is either white against the blue-grey background, or a dark grey/black against a white background, in order to keep the clean, crisp look throughout the site.

### Typography

Fonts are imported into the CSS file via Google Fonts.

To keep up with the clean and neutral look of the site, I chose to use just one font that is easy and simple to read.
I have chosen to use the font family of 'Montserrat', with a fallback font of 'san-serif', in the event of the preferred font failing to import. This font will hopefully create a positive user experience when first entering the site as it exudes a professional yet simplistic mood.

![Monseratt font](documentation/images/features/font.jpg)

### Imagery

Photographic imagery is used in some parts of the site. The landing page consists of a header, background image and a footer. The image has been slightly darkened and the opacity reduced so that it wasn't too vibrant against the subtle colours of the header and footer.

This image gives the user a good idea of what the site is about upon entering. The appealing image of fresh food should give the user motivation to explore the site further.

The Recipes page that contains all of the users' recipes consists of 4 diet specific categories. Each category has a card element containing an image related to that category, e.g. an image of a vegetable curry for the vegetable category.

The Manage Categories page consists of 4 images for each category, these images are the same for each category for ease which I may change at a later date.

![Various Imagery](/documentation/images/features/imagery.jpg)

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



![Manage Categories Page Wireframe](/documentation/images/wireframe-imgs/managecategories.jpg)

## Features
### Existing Features
Logo - located in the top-left of the header, the logo acts as a link to the landing page. As the header is fixed and visible at all times, the user can use either the logo or the nav menu to go back to the home section (top of the page)
Logo

Navigation bar - Sticks to the right side of the header which is fixed to the top of the page at all times. As this is a one page website, this will make it easier for users rather than having to scroll between in section. Hover effect creates a bottom border with a green colour to match the green colour that is often used throughout the page.
Navbar

Landing Page - On first entering the site, users will be drawn to hero image of the singer. This image uses warm colours and has a 'friendly' feel to it that invites the users in. From here they can easily navigate the site via the navigation menu or by scrolling.
Images - Large background images (photographs) will draw the users' attention as they are brightly coloured and bold against the subtleness of the webpage. The images bring a "fun-ness" to the site, creating a positive emotional response.
Text - Paragraphs throughout the site provides the user with some basic information about Jess, including her achievements and what she has to offer.
Contact icon - An envelope icon is centered half way down the page, below the events services section, so that users can click this icon and be directly taken to the contact form.
Videos - YouTube videos that Jess has recorded in her home studio are embedded via iframes, so the user can see what sounds and styles Jess brings to the table.
Contact form - A static contact form is in place, currently sourced by HTML and CSS only. Any message submitted currently will be posted to the Code Institute form dump. After aquiring the skills to enable to me to make this an active form, users will be able to contact Jess via email with any enquiries that they may have.
Contact form and Footer

Footer - The footer is fixed so that social media links are visible and accessible at all times. Links are opened in a new tab. Currently the links will only take you to the social platforms home page, eventually I would like to link these up with the clients' social media accounts.

### Features yet to implement
The logo is currently made using HTML text and CSS styling. I would like to aquire the skills to design and create a logo so that it could be embedded as an image.
I would like to add some sort of interactive system, such as calendly, to select a wedding package or event service so users can set a date with Jess in accordance to her calendar.
The videos as they are now clash quite a bit as they have different images when static. I would like to create an overlay that sits on top of the video, before being interacted with, so that they are of a consistent and common theme and colour, such as a background colour with the title of the song being sang in the video.
The contact form currently sends any messages submitted to the CI form dump, this is because this project is purely based on HTML and CSS. I would like to set the form up so that the client can receive emails from users.
Verification or feedback for the user after a message has been submitted on the form.

## Technologies Used
### Languages
HTML - Used to build the main structure of the webpage.
CSS - Used to style the content of the webpage.

### Libraries
Hover.css - Used in the nav menu, submit button and all icons when hovered over (nav menu - bottom border, icons and button - change of colour)
Google Fonts - Imbedded in the CSS, Google fonts are used in the header and body of the project.
Font Awesome - Icons used for social media links as well as a link directly to the contact form.
Balsamiq - Used to create wireframes for the project.
Chrome Dev Tools - Heavily used to fix any spacing issues as well as testing responsivity.
Github - To store repositories and codes after being pushed on Gitpod.
Git - Used for version control and tracking changes made to files.
Gitpod - Used for the workspace for this project.
Multi Device Mockup Generator (techsini) - To create an image of what the project will look like on various devices. TechSini.com
WebAIM Contrast Checker - To test colours throughout the site for whether or not they will produce good user experience.
W3C Markup Validator - To check for any HTML or CSS errors. There were some errors such as open tags or incorrect CSS values. These were all corrected and the project was fortunately left with 0 errors.
Testing
Most testing was carried out via Google Chrome browser and the Chrome Dev Tools for responsivity and colour contrast checking, throughout the process of building the project. I also tested the site on an iPhone 12 for responsivity, this included Google Chrome which showed no errors, and on Safari which did show some issues regarding the background images that would often stick when scrolling. Additional testing was carried out which I will include below.

## Manual Testing
Navigation

All navigation links take user to the correct section within the page.
All navigation links have a green underline and a bolder text when hovered over.
Clicking the logo takes user back to the landing page.
Navbar stays to the right of the header and responds well to different screen sizes.
Events List

The dashes between each list item disappears when viewing on a mobile, as the list items are being displayed as columns.
Contact Icon

Clicking the icon takes users directly to the contact form.
Changes size to suit different screen sizes.
Iframes/Videos

Videos do not play automatically when first entering the site.
Videos play with no errors when clicked.
Full screen option is enabled and works with no issues.
Responsive with different screen sizes. Videos are displayed in a row for larger screen sizes and columns for smaller sizes.
Contact Form

All input elements that have the required attribute are working as they should.
The email address input element requires an @ for it to be valid.
An error message appears if the inputs fields are not filled out appropriately.
The page refreshes when the form has been filled out correctly and the submit button clicked.
The submit button is clickable. Once I have aquired the skills to do so, I will create a modal or feedback of some sort that lets the user know that their message has been successfully sent.
Social Media Links

All icons are clickable and take the user directly to the homepage of the specified social media platform. These will be linked up to the clients' own business social media accounts once the website is made to be genuine and accessible for the client.
All href links have been entered correctly.
Links open a new tab successfully.
As well as Google Chrome and Safari, I have also tested the site on Firefox and Microsoft Edge. No issues or errors were identified and all content responded to different screen sizes as intended.

### Additional Testing
I used the a11y Contrast Checker to test all colours throughout the project. As you can see there has been one problem detected with the soft green colour I used for my h5 subtitles, the 'Music' text in the logo and the background colour of the contact form. I am happy to leave these colours as they are as I want to create a soft, subtle look to the entire site. By changing this soft, green tone to a more contrasting and vibrant tone, I fear that the intended look will be lost. After further testing on different screens, I can confidently say that the subtitles are easily read-able, and the form is easily seen, and are not at all lost in the background colour.

Colour Contrast Checker

I used the W3C Markup Validation and the W3C CSS Validator to ensure that there were no syntax errors throughout the project.

W3C Markup Results
W3C CSS Results
User Story Testing
User Story Testing

## Known Bugs and Fixes
During the process of building my project, I couldn't help but notice a vertical white space down the right side of the page (top to bottom), this was affecting the content and creating spacing and alignment issues.

After doing some research online and speaking with a tutor, this was resolved using the following code:

Credits are included in the CSS comments and in the Credits section of the README file.

Code to fix whitespace

HTML lines 6-12

When using the W3C Markup Validator, I received multipe warnings stating that the comments in my HTML code had more than 2 hyphens "!--------".

This was resolved by removing the hyphens and leaving only 2 before and after the comment.
An attribute of rel="noopener" was given to all untrusted external links, to improve best practise.

As the footer is fixed to the bottom of the page, this meant that the bottom of the contact page would become hidden by the footer.

This was resolved by creating a spacer div and adjusting the height accordingly with the different screen sizes.
When creating the media queries I could not understand why the the responsivity was poor and the text was overlapping each other quite quickly when using Chrome Dev Tools to test.

After speaking about this with my mentor, Felipe Souza Alarcon, he recommended that I don't use fixed heights for some of the elements, including the divs that were overlapping. Once I had gone back through the CSS and changed the height and width of certain elements, the problem was resolved.

## Deployment
This project was created using Gitpod, which enabled me to stage and commit the files via Git (version control) and pushed into the respository on Github.

To deploy the project on Github:
Select the repository you wish to deploy.
Click the Settings tab within that repository.
In the Settings, scroll down and select Pages.
In the Source section, click Branch and select the main option, click Save.
The URL for the deployed project is now saved in Pages.
Forking the Github Repository:
Choose to fork the repository by making a copy. You can then make changes to the copy without it affecting the original repository.

Select the repository you wish to fork.
In the top right corner of the page (under your account icon) there will be an option to Fork.
By selecting Fork you will now have a copy of the respository in your own Github account.
Cloning the Github Repository:
Select the repository you wish to clone locally.
Above the files, locate the Code dropdown menu.
Select and copy the link appropriately (HTTPS, SSH, Github CLI).
Open the terminal and change the directory to where you want the cloned version to be located.
Type git clone and paste the copied link.
Press Enter to create local clone.

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