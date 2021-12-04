# Duncan's Delicacies 



This site has been developed for the purpose of allowing the site owner an avenue to grow a community of budding chefs, where they're able to upload their own recipes in detail along with images of their creations. 

The site allows the owner to be able to gather data from their users, predominately their email address, meaning they can correlate a mailing list, growing their reach organically and keeping in touch with their growing community. 



The site offers users, both unregistered and registered, the ability to view user submitted recipes for themselves to follow along and create their own dish through thorough recipe instruction. 



This site is built for a budding chef, an experienced chef or anyone who likes to move away from instant noodles. 



## Features 



The site includes features which allow users to be able to view the 'Recipe Collection', register to the website allowing them the ability to add their own recipes. 

Once registered they can then edit their own recipes from their own profile page, which highlights their own submissions. It also allows them the ability to delete any submissions should they wish to. 

The goal for this website is to build a community of food enthusiasts who can share and take part in cooking all types of recipes they might not have adventured into. 



# Navigation



## Landing Page



The first page the users land on is the recipe collection page which enables them to select which recipe they'd like to view more of based on the course of the meal. 



It includes 3 large buttons with a background of a corresponding dish for that course. Keeping them large meant an affirmative first impression with the user, by including a ":hover" feature, the user knows to interact with the button once their cursor goes over it. 




The landing page also includes a nav bar which details the name of the website, as well as the pages available to the unregistered/not logged in user. 

A consistent colour scheme throughout the site enables the user to easily establish the interactivity of the site, as well familiarity once they get to use the site more. 



## Log In Page



The Log In page displays to the user a clear and concise log in form, which asks for both their 'Username' and 'Password', along with a link below which if the user isn't registered, they can click and it'll take them to the registration page. 



If the user is registered, they can enter their details and gain access to the inner workings of the website. 



## Registration Page



The Registration page displays a clear registration form, asking for their 'Username', 'Email', and 'Password'. 

If they select three valid entries, they'll be given access to the inner workings of the website, along with a welcome email automatically set up to work once a user has registered. 



If a registered user finds themselves here, they can find a link underneath the form which gets them back to their log in page. 



## Profile Page



Depending on the path in which the user has taken to gain access, they'll be  greeted by their own profile page. 

Should a newly registered user join, they'll be greeted with a 'Registration Successful' message at the top of the page. 



Should an already registered user login in, they'll be greeted with a welcome message, along with their username included. 

If that user has already submitted some recipes, the profile page is where they'll be able to Edit and Delete their own submissions. 



## Recipe Collection



By moving to the recipe collection, once you've picked your course of choice, you'll be greeted by already submitted recipes, housed within a collapsable accordion, an efficient way to maximise content without compromising screen space. 

Should the user click on the title of the recipe, they'll be given a full indepth description of the recipe, including how to complete it from start to end. 



The user will also be greeted with a search function which uses the parameters of both description and name to return results. 

Should a user be successful in finding a keyword, they'll be given all corresponding results. 
If however they don't, they'll be given a 'No Results Found' message, where they'll need to either press back in their browser, or a 'Back to Recipes' button underneath. 



## Add Recipe Page

Should a user finally muster up the courage of adding their own recipe, they'll be greeted with a recipe input form, which includes placeholders for example entries, details of the quantities, suggestions on how to appopriately enter data in certain fields, as well as provide a direct URL to their picture of choice to go along with their submission. 



The form has various parameters, and required fields which means that every recipe is submitted with all the neccessary information to ensure a positive user experience. 



Once they submit their recipe, and it's successful, they'll be redirected to the recipes page. 
Should they submit an invalid or incorrect form, they'll be kept on the page and informed of the issues through an alert box. 



## Log Out Page



Once the user has felt they've had enough of being on Duncan's Delicacies, they can choose to log out and clear their session, which greets them with a personal message and redirects them back to the log in page. 



# Deployment



This project was developed using gitpod, mongoDB and deployed on Heroku. 



In order to get this site fully functioning you must first:

#### GitHub and GitPod

1. Sign up to GitHub and create a repository, where it will build a workspace. 
2. Sign up to GitPod and connect your GitHub profile to it. 
3. Using GitPod.io as opposed to GitHub, it allows you to include and save the env.py file which enables the deployment further along the line with Heroku.
4. Create and populate your GitPod workspace with a Procfile, env.py, requirements.txt, and .gitignore files.
5. Save all files locally and push these files with their contents to your github repository. 

#### MongoDB
1. Sign up to MongoDB and create your first cluster. 
2. Within your first cluster, create your first collection (this will be your database).
3. Setting up your MongoDB to work with your own profile, and an I.P. of 0.0.0.0 and a port of 5000, along with your own administrator profile including a password (not to be confused with your mongoDB account password). This will go along with connecting your env.py file later on. 
3. You must then traverse to the 'Connect' heading in your database deployments where you will first need to connect your editor (GitHub/GitPod) with the MongoDB shell. 
4. Once they're completed, you can then move on to connecting your application by copying the driver code given to you and placing it in your env.py file on workspace. You will need to replace the password field and database name fields in order for the database to connect. 


#### Heroku
1. You must first have access to the GitHub repository. 

2. You must then sign up to Heroku and create an app, where you will then go to Settings - Reveal Config Vars, make sure the appropriate config vars are included. 

   - I.P : 0.0.0.0

   - MONGO_DBNAME: "Your MongoDB database name"

   - MONGO_URI: "An individual code to connect your MongoDB including your password and database name"

   - PORT: 5000

   - SECRET_KEY: "An individual secret key generated by a website will suffice"

3. Once this is included, you must go to 'Deploy' in Heroku, connect your repository through GitHub. 
4. Enable Automatic Deploys once connected. 
5. You can then Deploy Branch where it will build your site.

Once this is all completed, you should be able to have an external address which can be shared with others. 

## CREDITS

### FontAwesome
All my icons are from https://fontawesome.com/

### GoogleFonts
All my fonts are from https://fonts.google.com/ 

### EmailJS
Providing ultimate interaction between user and business was utilised by using https://www.emailjs.com/ API framework of building email templates and automated systems. 

### Materialize
I used the framework from https://materializecss.com/ in order to customise the look and feel of this website. 

### Images
3 images used in the recipe page, were found from www.pexels.com and all other images will be user submitted. 


