## Email_sender app:
**Concept**: This app uses Django for its backend function and employs javascript and html for its front end. You can send, update, delete and view mails with this.
## Directory Strucutre 
- **manage.py**: The main Django file which is run.
- **Email functionality**:
  - __init__.py
  - asgi.py
  - settings.py: This file contains necessary configurations for the project.
  - urls.py: This file contains the different URLs for different apps.
  - wsgi.py
- **Static**:
  - **css/style.css**: Contains generic CSS that applies to the whole app.
- **Templates**:
  - **Layout.html**: Contains the generic layout from which all other templates inherit.
- **Users**:
  - This app handles user creation/login/logout.
  - __init__.py
  - admin.py
  - apps.py
  - tests.py: Contains the necessary tests for the app.
  - forms.py: Contains the necessary forms for the app.
  - models.py: Contains the necessary models.
  - urls.py: Contains all the URLs to be directed to.
  - views.py: Contains the necessary views for the app.
  - templates/users:
    - **homepage.html**: This defines the layout for the homepage.
    - **login.html**: Defines the layout for the login page.
    - **registration.html**: Defines the layout for the registration page.
- **email_functionality**:
  - This app handles the functionality of sending/displaying/updating/deleting mails.
  - __init__.py
  - admin.py
  - apps.py
  - tests.py: Contains the necessary tests for the app.
  - forms.py: Contains the necessary forms for the app.
  - models.py: Contains the necessary models.
  - urls.py: Contains all the URLs to be directed to.
  - views.py: Contains the necessary views for the app.
  - templates/email_functionality:
    - **dashboard.html**
    - **drafts_view.html**
    - **mail_details.html**
    - **update_mail.html**
    - **write_mail.html**
- **.gitignore**: Contains files/directories to ignore.

## Setup Instructions

1. **Pull this project** into your directory where you have Django installed.

2. In the `settings.py` file, you'll need to configure the following settings:
   ```python
   EMAIL_HOST_USER = 'your-email'
   EMAIL_HOST_PASSWORD = 'token'

   ## How It Works

1. **Create an Account:** Start by creating a user account.

2. **Send Emails:** Send new emails to your recipients.

3. **Send Edited Emails:** Modify and send edited versions of emails.

4. **Delete Emails:** Remove emails from your database. Please note that this action won't delete the emails from the recipient's inbox.

This is how the project works, allowing you to manage emails effectively.
