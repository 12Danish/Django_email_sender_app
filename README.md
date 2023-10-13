# email_sender
This app allows users to create accounts. Send mails. Send Updated versions and delete requests. It uses the power of django to create and maintain databases and also employs the use of javascript to manage the frontend

Directory structure:
- Email functionality:
      - __init__.py
      - asgi.py
      - settings.py:
                   This file contains necessary configurations for the project
      - urls.py:
                   This file contains the different urls for different apps
      - wsgi.py
- Static:
      - css/style.css:
                      Contains generic css which applies to the whole app
- Templates:
      - Layout.html:
                    Contains the generic layout from which all other templates inherit
- Users:
       This app handles user creation/login/logout.
      -__init__.py
      - admin.py
      - apps.py
      - tests.py: Contains the necessary tests for the app
      - forms.py: Contains the necessary forms for the app
      - models.py : Contains the necessary models
      - urls.py : Contains all the urls to be directed to
      - views.py : Contains the mecessary views for the app 
      - templates/users :
                         Contains the necessary template files
                         - homepage.html: This defines the layout for the homepage
                         - login.html: Defines th layout for the login page
                         - registration.html : Defines the layout for registration page
  - email_functionality:
                       This app handles the functionality of sending/displaying/updating/deleting mails
                  
  
