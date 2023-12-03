<h1 align="center">Los Platos Chileno Restaurant App</h1>

[View the live project here.](https://los-platos-chilenos-845fa18371a9.herokuapp.com/)

This is a fictive restaurant booking app which is developed based on user stories and with a focus on responsiveness and accessibility.

<h2 align="center"><img src="https://bild på app i olika format"></h2>

## User Experience (UX)

- ### User stories

  - All user stories can be found on GitHub in a project specific Kanban board. [Visit Project](https://github.com/users/Pernilla-Strandberg/projects/2)

## Features

- Responsive on many device sizes - Built with Bootstrap 5 and tested along with development for small, medium and large screens.

- Seamless reservation process - Easily book a table at your favorite restaurant with a simple and intuitive reservation process. Users can select the date, time, and number of guests to secure their dining experience hassle-free.

- Automated unit tests - Assures the form, view and model files response as expected so that the user's experience is as simple and positive as possible.

<img src="![Admin view](readme_img/admin.png)"> <img src="https://bild på app i olika format"><img src="https://bild på app i olika format"><img src="https://bild på app i olika format">

### Upcoming features

- Google Map implementation to show restaurant location.
- Bookable times should only be displayed if they have not already been booked.
- Newsletter signup
- Possibility to book a table in a special place such as by a window
- Directions by bus and/or car 

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Django 4.2.7](https://docs.djangoproject.com/en/4.2/releases/4.2.7/)
   - Django was used to build the app. Example of installed and/or used libraries: gunicorn, dj_database_url, psycopg2, urllib3, django-crispy-forms.
2. [ElephantSQL](https://www.elephantsql.com/)
   - ElephantSQL was (is) used as external database.
3. [Heroku](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
   - Heroku was (is) used to deploy the app.
4. [Bootstrap 5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
   - Bootstrap 5 css was used to assist with styling and responsivenes for layout and forms. Also, Bootstrap icons was used as icon library.
5. [Google Fonts](https://fonts.google.com/)
   - Google fonts were used to import 'Ephesis' as display font, 'Roboto' and 'Lato' as content fonts.
6. [Git](https://git-scm.com/)
   - Git was used for version control in Gitpod terminal to handle commit and pushes to GitHub.
7. [GitHub](https://github.com/)
    - GitHub stores the projects code and also has user stories connected to the project.
8. [Mage](https://mage.space)
    - Mage was used to create all AI generated images on the page.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flos-platos-chilenos-845fa18371a9.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv#errors) mainly according to imported bootstrap css min file.
- [W3C Markup Validator](https://validator.w3.org/nu/) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flos-platos-chilenos-845fa18371a9.herokuapp.com%2F) few errors and some warnings will be handled in the near future

### Automated testing

    #### PYtest - Errors to be fixed in the near future
    <h2 align="center"><img src="https://bild på tester"> <img src="https://bild på tester"></h2>


### Manual testing

    #### Browsers and different screensizes
    <h2 align="center"><img src="https://bild på tester"> <img src="https://bild på tester"> <img src="https://bild på tester"></h2>

### Further Testing

- Friends and family members tested the app and pointed out some bugs that are presented under "Known Bugs".

## Deployment

The project was deployed to Heroku:

1. Connect GitHub repository to Heroku app
2. Set up basic dyno and add "gunicorn projectmap.wsgi" for webb
3. Add Config vars:
- CLOUDINARY_URL
- DATABASE_URL
- PORT
- SECRET KEY
4. Deploy automatically or manually and open app


## How to run it

1. Locate [GitHub Repository](https://github.com/Pernilla-Strandberg/django-restaurant-app)
2. Fork or Clone repository
3. Open project in vs-code or another source code editor
4. Configure environment variables in projectmap/settings.py
5. Install all necessary packages: $ pip install -r requirements.txt 
6. In settings DATABASE, switch back to Django db.sqlite3 as default
7. Run server: $ python manage.py runserver
8. Create a booking, login to change or delete booking.


## Credits

### Code

- [Mage](https://www.mage.space/) - All images is created in Mage AI tool

- [Bootstrap5](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - Bootstrap Library used for layout and forms

- [MDN Web Docs](https://developer.mozilla.org/) - To get a better understanding of views, models and templates, [this tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website) was great. I modified a lot of the provided code to fit my booking app.  

- [Medium](https://medium.com/) - Health Clinic Appointment tutorial that helped me a lot with the logics according to views and models [Healt Clinic Tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)

### Content

- All content was written by me (the developer).

### Media

- All Images were created by me (the developer).

### Acknowledgements

- Code Institute project walktroughs and the included pedagogical content.
