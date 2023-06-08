
<h1 align="center">Bod Fitness Personal Training Booking Website - Project Portfolio 4</h1>

![GitHub last commit](https://img.shields.io/github/last-commit/bodthegod/bod-fitness?color=blue&style=for-the-badge)

![GitHub contributors](https://img.shields.io/github/contributors/bodthegod/bod-fitness?color=green&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/bodthegod/bod-fitness?color=orange&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/bodthegod/bod-fitness?color=brown&style=for-the-badge)
## - By Joe Playdon

### [View the live project here](https://bodfitness.herokuapp.com/) #
### [View the repository here](https://github.com/bodthegod/bod-fitness) #

# Table of Contents:
1. [About the project](#about-my-website)
    1. [First Time Visitor Goals](#first-time-visitor-goals)
    2. [Returning and Frequent Visitor Goals](#returning-visitor-goals)
2. [Design](#design)
    1. [Colour Scheme](#colour-scheme)
    2. [Typography](#typography)
    3. [Imagery](#imagery)
	4. [Wireframes](#wireframes)
	5. [Features](#features)
    6. [Features Importance Table](#features-importance-table)
    7. [Screenshots of Features](#screenshots-and-features-within-website)
    8. [Structure](#structure)
    9. [CRUD Table](#crud-table)
3. [Languages and Resources](#languages-used)
4. [Techologies Used](#technologies-used)
5. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories-from-user-experience-ux-section)
    2. [HTML Validator Results](#html-results)
    3. [CSS Validator Results](#css-results)
    4. [Lighthouse Reports](#lighthouse-reports)
    5. [Further Testing](#further-testing)
    6. [Manual Testing](#manual-testing)
6. [Bugs and fixes](#known-bugs)
7. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking Repository](#forking-the-github-repository)
    3. [Making A Local Clone](#making-a-local-clone)
8. [Credits](#credits)
    

![Website Designs](/readmeimages/readmepreview.PNG)</h2>

### About my website

This is my personal training booking website, where users can select dates of which they want to book a session with different advice choices.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to be able to easily navigate the website, and register an account. 
        2. As a First Time Visitor, I want a simple and easy and UI that is fully functional and gives me the choice to book a session once logged in. 
        3. As a First Time Visitor, I want to see the dates that are available for personal training sessions.
        4. When visiting the website for the first time, I want to be able to book a session and view my bookings easily.
        5. Any First time user would like to check when their bookings are for, easily accessed by a dropdown menu.
        6. As a first Time Visitor, I want the process of booking a session to be as intuitive as possible.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to easily login. 
        2. As a Returning Visitor, I want to be able to view my upcoming sessions.
        3. As a Returning Visitor, I want a simple UI that is easy to navigate and easy on the eye.
        4. As a Returning Visitor, I want the ability to logout.
        5. As a Returning Visitor, I would like to view social links.

    -   #### Frequent User Goals

        1. As a Frequent User, I want the website to remember my details so that I can login. 
        2. As a Frequent User, I want to be able to check my previous bookings and future bookings. 
        3. As a Frequent User, I want the creator of my website to be able to see when I am booked in for. 
        4. As a Frequent User, I want the booking process to be as easy as possible. 

    -   ### Design

    -   #### Colour Scheme

        -   The main colours in the frontpage I have used are light grey for the navbar, to give a slight shade to imply to the user where the top of the page is- keeping the overall theme of the website very sleek and simple. Within my navbar, the title of the website is in black and a bold font choice, to maintain heirarchy on the page and the nav text is grey to keep it easy on the eye. For the headers and text, I have used the colour #303030 which is a common colour choice within UI designers to prevent eye strain against a white background, yet again making my website easier on the eye. I have used a consistent colour scheme throughout every page of my website, and a simple blue colour (#0d6efd) for the majority of buttons to show emphasis to a user. Finally- I have used a sleek #212529 (dark grey) for the footer, which is displayed across all pages- the text inside the footer is in white, and the social links displayed in the same blue as the buttons (#0d6efd) purely to keep the styling and imagery consistent. I enjoy looking at the front page because it is very easy to understand what the website is for and how to go about using it.

        Furthermore, for the login page I have used the #303030 colour for the heading and text, the same blue from the inital buttons (#0d6efd) for the "Sign In" button and this blue colour inherited for the "register an account" anchor tag.

        Moreover, for the register page I have used the same colours inherited from the login page, however the "Sign Up" button is green (#198754) to signify a positive change to the user when submitting the register form. Yet again, the anchor tag to redirect a user to the "sign in" page is in blue.

        Finally, in terms of the authentication section of my website, the logout section uses the same styles as the previous login/register pages- however a red colour (#dc3545) is used to display to the user that this action will have an impact on the login status, and log them out. Throughout all pages this colour scheme is consistent and it completes the user experience.

    -   #### Typography

        -   I have chose the Space Grotesk font as the main font used within all of my website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site from the external link. Space Grotesk is a nice font choice for a modern and simple website, and I had looked around on UI design websites for good font choices, allowing me to choose this. This is very appropriate for my website as it is easy to read, bold and attractive to view. I have kept this font choice throughout my website to keep the styling consistent and familiar.

    -   #### Imagery

        -   I did not feel as if it was necessary to use any external images within my website, to keep it simple and easy on the eye. I feel as if adding images to this would add too much clutter and cause an overload for the user, so I kept it simple and stuck to text and intuitive buttons. I personally feel from a user standpoint images would take away from the simplicity of booking personal training sessions. 

    *   ### Wireframes
        
    -   I have used [Balsamiq Wireframes](https://balsamiq.com/) as my desired wireframing tool for my website, as it is very easy to use. However, due to these being wireframes, the final image of the website may be depicted differently yet these are base guidelines of my website, and the image I would like to achieve. Here I have created Home page, Register page, Booking and finalise booking page, Sign in, Sign out, My bookings and Admin bookings wireframes. I have made wireframes for both mobile and desktop views of the website.

    -   Home Page Desktop Wireframe - [View](/readmeimages/wireframes/home-page-desktop.png)

    -   Home Page Mobile Wireframe - [View](/readmeimages/wireframes/home-page-mobile.png)

    -   Register Page Desktop Wireframe - [View](/readmeimages/wireframes/register-desktop.png)

    -   Register Page Mobile Wireframe - [View](/readmeimages/wireframes/register-mobile.png)

    -   Login Page Desktop Wireframe - [View](/readmeimages/wireframes/signin-desktop.png)

    -   Login Page Mobile Wireframe - [View](/readmeimages/wireframes/signin-mobile.png)

    -   Logout Page Desktop Wireframe - [View](/readmeimages/wireframes/sign-out-desktop.png)

    -   Logout Page Mobile Wireframe - [View](/readmeimages/wireframes/sign-out-mobile.png)

    -   Booking Page Desktop Wireframe - [View](/readmeimages/wireframes/booking-page-desktop.png)

    -   Booking Page Mobile Wireframe - [View](/readmeimages/wireframes/booking-page-mobile.png)

    -   Finalise Booking Page Desktop Wireframe - [View](/readmeimages/wireframes/finalise-booking-desktop.png)

    -   Finalise Booking Page Mobile Wireframe - [View](/readmeimages/wireframes/finalise-booking-mobile.png)

    -   My Bookings Page Desktop Wireframe - [View](/readmeimages/wireframes/my-bookings-desktop.png)

    -   My Bookings Page Mobile Wireframe - [View](/readmeimages/wireframes/my-bookings-mobile.png)

    -   All Bookings (admin) Page Desktop Wireframe - [View](/readmeimages/wireframes/admin-bookings-desktop.png)

    -   All Bookings (admin) Page Mobile Wireframe - [View](/readmeimages/wireframes/admin-bookings-mobile.png)

    -   Why Us Page Desktop Wireframe - [View](/readmeimages/wireframes/whyus-desktop.png)

    -   Why Us Page Mobile Wireframe - [View](/readmeimages/wireframes/whyus-mobile.png)

    -   Edit Booking Desktop Wireframe - [View](/readmeimages/wireframes/edit-booking-desktop-wireframe.png)

    -   Edit Booking Mobile Wireframe - [View](/readmeimages/wireframes/edit-booking-mobile-wireframe.png)

    -   Edit Success Desktop Wireframe - [View](/readmeimages/wireframes/edit-success-desktop-wireframe.png)

    -   Edit Success Mobile Wireframe - [View](/readmeimages/wireframes/edit-success-mobile-wireframe.png)



    ## Features

-   Home page with "Register" button on front page, allows the user to instantly have a link to the main function of the website (creating an account to book sessions). When user is authenticated, the home page button changes to "Book a session"

-   Nav bar with content that changes depending on if the user is authenticated, options changing from "Register" and "Login" when not authenticated to a "Bookings" dropdown menu with options being "Book a session" and "My Bookings". If user logged in is a superuser, "My Bookings" changes to "All Bookings", allowing for the admin to have a frontend view of every booking. "Logout" is also shown when the user is authenticated, to signify to the user that they are currently logged in.

-   Booking page, allowing for the next monday, tuesday and wednesday within the next 7 days to be displayed. If a day is already booked, the python function will remove this day from being displayed to the user so that there is no confusion about what days are booked. The user can also select from multiple advice topics, and choose wether the session is in person/online. When all 3 days are booked, the website displays "no days available" within the "select your day" dropdown menu, and I have set the confirm booking button to disabled when there are no days available. This prevents confusion to the user- and is good UI practice when developing a system like this.

-   Once a user books in a session, they are shown the finalise booking screen, which displays to the user all the options they had chosen, including the unique booking number, and the date that they have selected. From this page, there is a button that is displayed to allow the user to go to their bookings, or to take the user back to the previous page. 

-   If the user selects the button that redirects them to the "My bookings" page, this is where they can Read, Update or Delete their created records that were added to the database.

-   Due to time constraints and bugfixing, I hadn't implemented the admin front end interface to edit bookings, however a user can access all of this functionality for their own bookings. This allows for full CRUD functionality for the user.
### Features Importance Table

When first implementing the features for this website, I had brainstormed ideas and the importance that they would have on the User Experience when browsing my website, this is a brief features importance table:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | Create, View, Update and Delete Bookings | 5 | 5 |
| 2 | Login, Logout and Register Functionality | 5 | 5 |
| 3 | View My Bookings as a User | 5 | 5 |
| 4 | View All Bookings as an Admin | 5 | 5 |
| 5 | Create a "Why Me" Page | 3 | 2 |
| 6 | Require User Authentication for Bookings | 5 | 5 |
| 7 | Edit content if User is Superuser | 4 | 4 |
| 8 | Refine UI Designs | 3 | 2 |
| 9 | Validation of User Data | 5 | 5 |
| 10 | Create, View, Update and Delete User Accounts | 5 | 5 |
| 11 | Payment System for Bookings | 3 | 2 |
| 12 | Live Chat for Advice | 1 | 1 |

After analysing my table, I had decided to create a limited number of these features due to time constraints. The features I added were (1, 2, 3, 4, 5, 6, 7, and 9).

## Structure
### Flow Diagrams
Within my flow diagrams, I have annotated the layers of authentication for the user role within the website.

- The why me page is available to all users, and login and register are also available for all users, including unregistered accounts. 

- Once an account has been logged into or created, the nav bar elements will change based upon if the user is authenticated. The elements allow a user to create bookings, view their bookings and logout of their account. 

- If a user decides to view their bookings, this will only show them entries within the database regarding their user account. If a superuser is logged in, this button will show the admin all entries within the database. 

#### Unregistered User
![Unregistered User's Flow](/readmeimages/unregister-user-flow.png)

#### Registered User
![Registered User's Flow](/readmeimages/registered-user-flow.png)

#### Superuser
![Superuser's Flow](/readmeimages/superuser-flow.png)

### **CRUD TABLE**
This shows what CRUD functionality is available from each page
| Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| home |  | basic information regarding what the website is for |  |  |
| booking | create booking with choices and booking number | view available dates for bookings, choose advice topic and online or in person |  |  |
| finalise_booking |  | displays all booking information to user |  |  |
| account_panel |  | view all booking data for current user | edit booking data | delete selected booking from database |
| created_booking |  | requires superuser, view all booking data for all users (admin panel) | edit booking data | delete any booking from database |
| register | user profile |  |  |  |
| login |  | login with username and password |   |  |  |
| edit_booking |  | view booking data | edit booking data  |  |  |


### Defensive Programming
In order to keep my website secure and effective at keeping malicious attempts prevented, I implemented features alongside my project development to prevent this.
- I had used @login_required on functions and page renders that required a user to be logged in. 
- I used jinja templating like `{% if user.is_authenticated %}` and `{% if user.is_superuser %}` to enforce a specific user flow when navigating my website.
- The routes functionalities within my urls file also checks if a user is:
    * authenticated (logged in)
    * is allowed to request certain data, or submit a booking (required booking number) 
    * a superuser


### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)

-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Technologies Used

* [Cloudinary API](https://cloudinary.com/) was used to enable users to upload images whilst keeping the App safe and secure

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Flask was used to handle the templating for the site.

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used to store all user data, logins and data entries from the users.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [pipenv](https://pipenv.pypa.io/en/latest/)
    * I used pipenv to easily setup my working environment. In order to run my project, start by running the virtual environment with `pipenv shell`, then use `python manage.py runserver`

* [Jinja](https://www.palletsprojects.com/p/jinja/)
    * Jinja is a templating engine for Python, used to write Flask and other templating languages. I had used this to extend certain files and enable for block content to be changed.

* [Git](https://git-scm.com/)
    * Git was used for version control, editing and saving commits to push them to the repository that my project was hosted on, allowing for a history of commits to be viewed.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap was used for all the layout and general styling of my website, allowing my attention and focus within production to stay on the functionality and logic of my work.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * My project was created with chrome, and chrome dev tools were used in the production of my project.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where I have deployed the final and live version of my project. 

* [GitHub](https://github.com/)
    * GitHub is where all the code and commits to my project are stored.

* [Google Fonts:](https://fonts.google.com/)
    * Google fonts were used to import the fonts into the style.css file which is used throughout the whole project (maintains a certain style).

* [Font Awesome:](https://fontawesome.com/)
    * Font Awesome was used on The final score box for the finish icons and the time icon within the game area, and tick and cross icons.

* [Balsamiq:](https://balsamiq.com/)
    * Balsamiq was used to create the [wireframes](/readmeimages/wireframes/) during the design process.


### Resources Used


-   I have used the W3 [HTML](https://validator.w3.org/#validate_by_input) and [CSS](https://jigsaw.w3.org/css-validator/#validate_by_input) validator, the [CI Linter](https://pep8ci.herokuapp.com/), [JShint](https://jshint.com/) and occasionally the [W3Schools](https://www.w3schools.com/) resources when I had an issues.

-   For testing my website on different screen sizes, I used Google Chrome Dev Tools.

-   For testing my website on IOS, I used the app that I deployed to heroku to view and play around with it.

-   For styling inspiration, I used [ColorMind](http://colormind.io/bootstrap/)

-   For font styles, I used [Google Fonts](https://fonts.google.com/)

-   Colours were all checked with [Contrast Grid](https://contrast-grid.eightshapes.com/)

-   To create the favicons I used [Favicon.io](https://favicon.io/favicon-generator/)

-   To create the mobile responsiveness and look of the website, I used [Bootstrap](https://getbootstrap.com/)

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. In addition to this, I used Chrome Dev tools very often to play around with the code and test when I was having issues. I found this was extremely important when troubleshooting issues- as I could change the code and see the changes live, instead of having to save the file and force refresh (If I changed the CSS code). I had also used print statements to see what data was being submitted from my functions, and to troubleshoot certain issues I was having. 

The use of chrome dev tools allowed me to play around with the breakpoints for different screen sizes, and allowed me to view errors within the console when playing around with my website. 

## HTML Results

-   [W3C Markup Validator](https://validator.w3.org/)
-   [index.html Results](/readmeimages/index-html-validation.PNG)
-   [booking.html Results](/readmeimages/booking-html-validation.PNG)
-   [createdbookings.html Results](/readmeimages/created-bookings-html-validation.PNG)
-   [finalisebooking.html Results](/readmeimages/finalise-booking-validation.PNG)
-   [about.html Results](/readmeimages/why-me-html-validation.PNG)
-   [Sign In HTML Results](/readmeimages/login-html-validation.PNG)
-   [Sign Out HTML Results](/readmeimages/signout-html-validation.PNG)
-   [Register HTML Results](/readmeimages/register-html-validation.PNG)
-   [Edit HTML Results](/readmeimages/edit-html-validation.PNG)
-   [Edit Success HTML Results](/readmeimages/edit-success-html-validation.PNG)
-   When validating my HTML code, I used chrome dev tools to grab the code without the templating language to remove errors. This allowed me to validate all of the code when it was fully rendered, and when being extended from base.html.

## CSS Results
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [style.css Results](/readmeimages/jigsaw-validation.PNG)

## Python Resutls
-   [CI Python Linter](https://pep8ci.herokuapp.com/)
-   [Python Results](/readmeimages/python-validation.PNG)
-   I have validated all python files, however I could not include all of these in screenshots. All python files passed through the linter.
## JS Resutls
-   [JShint](https://jshint.com/)
-   [JS Results](/readmeimages/jshint-validation.PNG)
-   I have validated the JS code that is inline on my edit page.


## Lighthouse Reports

-   Lighthouse Report for Desktop - [View](/readmeimages/lighthouse-desktop.PNG)

-   Lighthouse Report for Mobile - [View](/readmeimages/lighthouse-mobile.PNG)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to be able to easily navigate the website, and register an account.

        1. When entering the website, the user is instantly shown a "Register and book now" button, allowing them to create an account.
        2. A register button is also displayed within the nav bar, for easy access.

    2. As a First Time Visitor, I want a simple and easy and UI that is fully functional and gives me the choice to book a session once logged in.

        1. This website is designed to be easy to navigate, and shows the user different things based upon their authentication status. This allows for the user to view a "Book Now" button which will replace the register button.
        2. There is an option to book inside the nav bar too, yet again proving easy for the user to navigate to the area they would like.

    3. As a First Time Visitor, I want to see the dates that are available for personal training sessions.

        1. When navigating to the booking page, the dates are easy to view for a user to book.
        2. The user can also only view dates that aren't currently booked by somebody, making it streamlined from a user standpoint.

    4. When visiting the website for the first time, I want to be able to book a session and view my bookings easily.
        1. This is simple to do as there is emphasis on booking, and the button is never taken away from the user on any page- as it is in the nav bar.
        2. The "my bookings" button is also always within the nav bar if the user is logged in.

     5. Any First time user would like to check when their bookings are for, easily accessed by a dropdown menu.
        1. The nav bar is always displayed for the user to view, and when clicking the "my bookings" button it shows them all of their upcoming, past or todays bookings.
        2. This information is compacted into links within the nav bar, inside of a simple dropdown button.
    
    6.  As a first Time Visitor, I want the process of booking a session to be as intuitive as possible. 
        1. This process is extremely simple as it goes: Book a session -> Finalise Booking -> My Bookings.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to easily login.

        1. The login button is always displayed within the nav bar, allowing for any user to simply log back into their account.

    2. As a Returning Visitor, I want to be able to view my upcoming sessions.

        1. This is possible to view within the "upcoming bookings" section of the "My Bookings" page. This displays to the user the date of their booking, and what it is for.

    3. As a Returning Visitor, I want a simple UI that is easy to navigate and easy on the eye.
        1. A returning visitor will be quite familiar with the layout of the website and due to the process being simple for them to book a session, it should reduce the time spent looking for the information and more time spent on the bookings.
        2. I have used specific blue buttons to guide the user through the process they desire through the website i.e booking a session.

-   #### Frequent User Goals

    1. As a Frequent User, I want the website to remember my details so that I can login.
        1. This is possible using the "remember me" checkbox when logging in.

    2. As a Frequent User, I want to be able to check my previous bookings and future bookings.
        1. This is possible within the my bookings section, saving all previous and future bookings for the user to view.

    3. As a Frequent User, I want the creator of my website to be able to see when I am booked in for.
        1. This is easily possible as there is a front end view of all bookings for a superuser to see.
        2. This section shows the superuser all bookings within the website, and the user's name.
        
    4. As a Frequent User, I want the booking process to be as easy as possible.
        1. As stated previously, the booking process is extremely simple for a frequent user to do- as all buttons have emphasis for finalising a booking.

### Further Testing

-   I tested my website on many different screen sizes using the inspect element web tool, which allowed for me to test specific breakpoints and the layout on different hardware.
-   I tested my website on Google chrome and Safari, as these browsers interacted differently and I had to plan accordingly by editing features for IOS.
-   I had tested all booking functions for mobile, and used different screen sizes so that I could create the layout accordingly.
-   I allowed my friends to test my booking functionality, account creation and authentication on the deployed project. This allowed me to fix bugs that they had found, as most of my time was spent developing the website.
-   I used Google Chrome Dev Tools to play around with css attributes to see a live display of the changes I made. This also displayed errors to me in the console, giving me an insight into why my website wasn't displaying correctly.

### Manual Testing

-    In this section, I will provide screenshots of tests I have done to ensure my project is fully functional with no bugs apparent to the user.

[Register and Book A Session Test Screenshot](/readmeimages/register-home-ss.PNG) This screenshot is relatively simple, and this is to test if the button that is clicked redirects the user to the regsiter screen, furthermore I have tested to see if this button, once clicked, changes to "Book a session" when the user is authenticated.

[Booking Test Screenshot](readmeimages/booking-ss.PNG) This screenshot shows the booking process, and how it displays information to the user. The user is shown the next monday, tuesday and wednesday within the next 7 days and when these are chosen, it disables the option to book as the sessions are all fully booked. 

[Finalise Booking Screenshot](readmeimages/finalise-ss.PNG) This screenshot tests wether the booking functionality fully works, as the booking submit button from the previous page was clicked, and the user is redirected to the finalise booking screen with all the informaiton they have submitted. This works correctly and all of the data is correct- with a unique booking number being assigned to the users booking.

[My Booking Test Screenshot](readmeimages/my-bookings-ss.PNG) I tested the functionality of the "my bookings" page by submitting a booking, and looking if it has been assigned to an upcoming, past or today slot. This functions correctly as all bookings that I have made were displayed.

[Delete Function Test](readmeimages/delete-function-ss.PNG) I have tested if I can delete records from the front end by clicking the delete booking button, this displays a message asking "are you sure you want to delete this", and I click yes. The booking from today was then deleted as displayed within this screenshot- as it is no longer displayed and the booking availability will open up for that day again.

[Edit Booking Test](readmeimages/edit-ss.PNG) I have tested all of the options that a user can select in order to edit their booking, and I have selected all options in order to manually test this. Initially I had bugs where the incorrect options were displaying, such as Strength Gain. I eventually solved this by changing the HTML file that it was stored in. 

[Edit Success Test](readmeimages/edit-success-ss.PNG) I have tested this page by confirming the edit of my booking, and it functions correctly- allowing the user to see that their edit was successful.

I have tested all of these functions on both an admin view, and a superuser view- which give different outcomes as I have allowed superusers to view every user booking, and users to only be able to see their own bookings. All functionality works as intended and there are no more bugs that I am aware of.

### Known Bugs

-   When creating the full functionality of my website, I came across many bugs, one of these was the E-mail section of my signup form not functioning correctly, which would display an error. This took away from the user experience and after a few forum posts and google searches, I added this line of code to my `settings.py` file to fix it. `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
`ACCOUNT_EMAIL_VERIFICATION = "none"`
This fixed the errors I was getting and allows the user to input their email and be correctly redirected to the home page. 
-   I have fixed a bug where the view all bookings page was not working as intended, as the data inside the database was not displaying. This took me about 4-5 hours in testing and bugfixing to find a workaround, however I managed to fix it by redefining how the data was displaying within the HTML files.
-   Naming conventions on cloudinary and local are different, as cloudinary assigns the image URL links to have `.png.png` at the end of the URL, if the image is defined as a png. This means that when hosting locally, a user would not be able to view the correct favicons due to cloudinary's naming conventions, and poor technology. This was a frustrating bug to find a workaround, which lead to me removing the `.png` in my media link tags.
## Deployment

### Heroku

To deploy this project, I have used Heroku.
The deployed version is the same as in the repository.
These are the steps used for deployment to Heroku:
1. In the console of the software you are using, inside the root directory of the project, run:
    pip3 freeze --local > requirements.txt
    to create a requirements.txt file containing project dependencies.
2. In the project workspace root directory, create a new file called Procfile, with a capital 'P'.
    Open the Procfile. Inside the file, check that web: python3 app.py has been added when creating the file
    Save the file.
3. Login to Heroku, select create new app, add the desired name for your app, make sure not to have any spaces, choose your closest region.
4. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
5. Navigate to the settings tab, click reveal config vars and input in the following:

| Key | Value |
| :---: | :---: |
| API_KEY | myapikey |
| API_SECRET | myapisecret |
| IP | 0.0.0.0 |
| PORT | 8000 |
| CLOUDINARY_URL | cloudinaryURL |
| SECRET_KEY | mysecretkey |
| DATABASE_URL | postgresql |

6. Go back to the Deploy tab and select enable automatic deploys
7. Click deploy branch
8. Click Open app once the build is complete

## Local Development
* How to Fork To fork the repository, use the following steps:
Login or signup to Github and locate the repository.
Click the Fork button in the top right corner
## Making Local Clone
Login or signup to GitHub and locate the GitHub Repository GitHub Repository.
Under the repository name, click "clone" or "download".
To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
Open the terminal in your preferred code editor and change the current working directory to the location you want to use for the cloned directory.
Type git clone, and then paste the URL you copied in Step 3.
Press Enter. Your clone will be created.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/bodthegod/bod-workout)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/bodthegod/bod-workout)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/bodthegod/bod-workout
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/bodthegod/bod-workout
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

-   To troubleshoot problems I had when defining media queries, I used [Stack Overflow](https://stackoverflow.com/questions/21441993/media-queries-doesnt-work)
-   Credits to my mentor Darío for encouraging me to continue to add things to improve my project.
-   Credits to this John Abdsho Khosrowabadi on inspirations of how to build my project [Dev Genius](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78), the function to loop through days was inspired by this project, and how to check if a day was selected. Initially I tried to take more inspiration from this project however my logic and functionality didn't work with the code written, so I had created my own.
-   Credits to this website for minimalist designs [Awwwards](https://www.awwwards.com/websites/minimal/)
