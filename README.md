# ONLINE COOKBOOK - MILSTONE PROJECT 3
 
#### Data Centric Development Project

In this project, we were asked to create an online Cookbook in where users could find recipes that includes, the cuisine, steps needed 
to take in order to cook, ingredients they will need and the required tools. We are to use backend code and frontend form(s) to allow
users to add their own recipes to the site, edit them and even remove them. Allow users to locate individual recipes based on specific
recipe fields. Provide results of the recipes that is easily accessible and visually pleasing for the user.

## UX DESIGN

This application gives Users the ability to browse through other peoples recipes, edit them, remove them and to add their own if they so choose.
The User will be able to see how long it takes to cook a specific recipe, what ingredients are used, the step by step guide on how to make
a specific recipe and what tags are associated with a recipe.

- I made some mockups before starting this project to get an idea of what my application could look like when it's fully complete, these can be found **[Here.](https://github.com/CapitainHolmes/cookbook-project/tree/master/mock--ups)**


### User Stories:

- As a User I want the ability to add reicpes to the application.
- As a User I want the ability to edit recipes on the application.
- As a User I want the ability to remove recipes from the application.
- As a User I want the application to be easily accessible and visually pleasing.
- As a User I want to see a step by step guide on how to make the meals.
- As a User I want to see how difficult recipes are to make.
- As a User I want to be able to see everything needed in order to make the meals correctly such as time length and ingredients.

## FEATURES

### Features Used in This Project:

- View the step by step guide on how to make the recipes.
- View the full list of ingredients needed to cook the recipe.
- See other bits of useful information about the recipe which include, cook time, how many people it serves and the difficulty level.
- A dropdown navigation bar for smaller sized screens.
- Able to add you're own recipe with image.
- Ability to edit an existing recipe.
- Able to delete unwanted recipes.

## TECHNOLOGIES

### The Technologies I Have Used:

- **[Moq Ups](https://app.moqups.com/)** - I have used MoqUps to create the mockup version of my website, that can be found **[Here.](https://github.com/CapitainHolmes/cookbook-project/tree/master/mock--ups)**
- **[HTML5](https://en.wikipedia.org/wiki/HTML5)** - I have used HTML5 to create the base of my project.
- **[Materialize](https://materializecss.com/)** - I have used Materialize for it's frontend frameworks for the style and layout of my project.
- **[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)** - I have used CSS3 for myy custom styles for certain things in my project.
- **[jQuery](https://en.wikipedia.org/wiki/JQuery)** - I have used jQuery to simplify my JavaScript.
- **[MongoDB](https://www.mongodb.com/)** - I have used MongoDB for my database to store all the recipe data.
- **[Python 3](https://www.python.org/)** - I have used Python 3 for the backend of my project along with the **[Flask Framework](https://en.wikipedia.org/wiki/Flask_(web_framework))**.
- **[Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)** - I have used Jinja2 for it's templating language so that i'm not repeating unnecessary code.
- **[Heroku](https://en.wikipedia.org/wiki/Heroku)** - I have used Heroku to deploy my application.

## TESTING

I conducted tests on a wide selction of browsers/devices to ensure User's can successfully use the site and it's features.

These tests included browsers/devices:

- Edge - laptop
- Mozilla - laptop
- Chrome - laptop and iPhone
- Safari - iPhone
- Internet Explorer - laptop
- I was forever checking the logs in the Terminal and Heroku to see that there were no errors and the application was not broken. This I found really useful for debugging issues as it states specifically where the problem is.
- Making sure the code runs wihtout issues using the **[Google Chrome Inspect](https://developers.google.com/web/tools/chrome-devtools/shortcuts)** Tools.
Inside Chromes Dev Tools I can:
    - Check the responsiveness for individual phones and screens, example, an IPhone/Samsung.
    - I can also change and adapt my code inside the Tools, to see what works and what doesn't. Also staying aware that these changes I make are not permenant.

### User Stories Testing

- "As a User I want the ability to add reicpes to the application." 
**This was tested by me by first, filling out a test recipe in the form provided on the Add Recipe page. Then selecting the Add Recipe button located at the bottom of the form, which then returned me to the Recipe page where my new test recipe was visable and was successfully added to the database.**
- "As a User I want the ability to edit recipes on the application."
**This was tested by clicking the edit recipe button on a test recipe card on the recipes page and then updating it with new details.**
- "As a User I want the ability to remove recipes from the application."
**This was tested by selecting the delete recipe button on a test recipe on the Full Recipes page and successfully removing the test recipe from the application and the database.**
- "As a User I want the application to be easily accessible and visually pleasing."
**This was tested by my friends and family who used the application, which they all said that they had no problems locating the necessary things on the application.**
- "As a User I want to see a step by step guide on how to make the meals."
**This was tested by first, selecting the Full Recipe button on a recipes card on the recipes page, which then redirected me to a page where I could see underneath the image was the 3 step guide on how to make the recipe.**
- "As a User I want to see how difficult recipes are to make."
**This was also tested by selecting the Full Recipe button on a recipes card on the recipes page, which then revealed the difficulty level of that recipe.**
- "As a User I want to be able to see everything needed in order to make the meals correctly such as time length and ingredients."
**This was also tested by selecting the Full Recipe button on a recipes card on the recipes page. The rest of the necessary information was also rendered straight from the database and I could see a list of ingredients, as well as the cook time and how many people that recipe serves.**


Here is a list of each Validator used to check my code:

- **[W3C HTML](https://validator.w3.org/)**
- **[W3C CSS3](https://jigsaw.w3.org/css-validator/)**



## DEPLOYMENT

Throughout the course of this project I have been commiting every finished functionality, 
every bug fix and things I thought needed removing, to GitHub using **[Version Control.](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)**

All my commits and the full code for my project can be found on my GitHub Repository which can be found **[Here.](https://github.com/CapitainHolmes/cookbook-project)** 

I have also commited and deployed my work to Heroku, which can be found **[here](https://cookbook-database-project.herokuapp.com/)**

## CREDIT

### Content

The content used in this project was all sourced from the **[BBC GoodFood](https://www.bbcgoodfood.com/)** site. This includes the recipes name, indgredients, 
the full recipe and pretty much everything associated with the recipe including the image.

## ACKNOWLEDGEMENTS

I recieved inspiration for this project from:

- Friends.
- My Mentor Juan.
- The BBC GoodFood Website noted above.