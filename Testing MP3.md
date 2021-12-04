# Testing



This documents accounts for the testing procedures that have taken place in order to demonstrate the functionality of this site. 



## Validator testing

### HTML

https://validator.w3.org/

The HTML error had no errors aside from the validator not recognising the jinja templating language which incurred it to highlight every jinja code. 

Other than that, all other HTML worked soundly. 



### CSS

https://jigsaw.w3.org/css-validator/

The CSS validator came back with zero errors. 





## User Stories



1. **As a new Visitor I want to be able to access the site quickly and efficiently.**

   *By using a clear and concise layout structure, the user is instantly greeted with the recipe collection page, which enables them to browse the submitted recipes without ever having to log in or register. They're also able to search for recipes using certain keywords.*

 ![recipe](/static/images/Testing/recipe-menu.png)




2. **As a new visitor I want to know what sort of website this is.** 

   *By landing the user on the recipe collection page, it straight away tells the user what this website includes*.

3. **As a new visitor, I don't want to see mountains of text which is difficult to read.**

   *Making sure that the content on this page is easy to read with contrasting colours was a key priority as there was real potential to overload with text due to the nature of the recipes being submitted, including lists of ingredients and directions for use.* 

   *By minimising all other text to a bare minimum, it means that when the user is confronted with a lot of text, it doesn't overly affect the UX in a negative way as it's a new interactive experience when confronted with a large amount of text on this site.*

4. **I want to add my own recipe but I don't want to spend ages registering and inputting all my recipe.**

   **Our registration process is quick and easy to work with. You can sign up with your email address and an available username in less than 1 minute.
   Once in, youll be able to add your own recipe on our interactive form which enables you to precisely put down individual values, quickly and efficiently.*

   

   # Testing

   Registration with a used username

   

  ![usernametaken](/static/images/Testing/username-taken.png)

   

   If a username is inputted which has already been chosen, the page informs the user that they need to use a new name. 

   

   ### Email Registration

   

   ![emailadmin](/static/images/Testing/email-to-admin.png)

   

   When registered, an email is sent to both the admin and the new user welcoming them to the website.

![emailuser](/static/images/Testing/email-to-user.png)
   

   ### Login with wrong credentials

   

![loginfail](/static/images/Testing/login-fail.png)
   

   If the user inputs an incorrect field, the login informs the user that either the username or password is incorrect. 

   

   ### Search Functionality

   

   ![search with results](/static/images/Testing/search-with-results.png)

   

   When a successful search query is met, results are displayed in a new search.html page. 

   

   ![search with results](/static/images/Testing/search-no-results.png)


   

   When an unsuccessful search query is met, results are not displayed and the user is informed that no results were found. 

   

   ### Add Recipe validation


   Inputting correct fields, results in green validation lines under the fields. 

   ![recipe validation](/static/images/Testing/recipe-add-form.png)

   Inputting incorrect values into the fields results in a red validation line under the fields

   When trying to submit the form, the browser sends an alert notifying the user of the fields requirements. 


   ### Edit functionality

   

   ![edit buttons](/static/images/Testing/user-edit-recipe.png)

   

   A user is greeted with their submissions and permissions in their profile, they're allowed to edit and delete.

   

   ![recipe delete](/static/images/Testing/user-delete-recipe.png)
   

   A delete request prompts the browser to make sure the user is sure they want to do it. A confirmation results in the submission being deleted. 

   

   ## Admin super user functionality

   

   ### Admin privileges 

   

   ![admin privilege](/static/images/Testing/admin-privileges-in-recipes.png)

   

   When the admin is confronted with the recipe pages, they are able to edit and delete the submissions, only once they've been amended by the admin will they display in the admin's profile. 

   
   ![admin privilege](/static/images/Testing/admin-privileges-in-navbar.png)


   ### Admin Categories

 
   ![admin privilege](/static/images/Testing/admin-manage-categories.png)

   ![admin privilege](/static/images/Testing/admin-add-category.png)

   ![admin privilege](/static/images/Testing/admin-new-category.png)
   

   As admin, the user has access to more features including the ability to manage categories, including adding, editing or deleting the categories. 

   ![admin privilege](/static/images/Testing/admin-category-edit1.png)

   ![admin privilege](/static/images/Testing/admin-category-edit-success.png)
   
   ![admin privilege](/static/images/Testing/admin-category-delete.png)
   

   If the Admin chooses to delete, they're prompted about the decision with an alert box in browser. 

   

   

