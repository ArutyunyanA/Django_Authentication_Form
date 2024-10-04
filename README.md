# Django Authentication Project

This is a basic Django project based on the first project from the book *"Antonio Mele's 4 Django Projects"*. It implements user authentication with forms and includes HTTPS support for secure connections. This project does not integrate third-party social network logins.

## Features

- User Registration
- User Login/Logout
- Password Change and Reset
- Secure HTTPS Connection
- Form Validation
- Profile management (optional)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/django-auth-project.git
    cd django-auth-project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.env` file**:
   Create a `.env` file in the root directory with the following environment variables:
   ```bash
   DEBUG=False
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=yourdomain.com

	5.	Configure HTTPS:
To enable HTTPS, you will need an SSL certificate. You can either:
	•	Use a self-signed certificate for local testing.
	•	Obtain a free certificate using Let’s Encrypt.
Then configure your server to use HTTPS. If you are using Django’s built-in development server for local testing, you can set the following in settings.py:

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


	6.	Apply migrations:

python manage.py migrate


	7.	Create a superuser:

python manage.py createsuperuser


	8.	Run the development server:

python manage.py runserver

For testing with HTTPS, use:

python manage.py runserver_plus --cert-file cert.pem

(You may need to install django-extensions to use runserver_plus.)

Project Structure

	•	accounts/ - Contains the authentication app with forms for login, logout, password change/reset, and user registration.
	•	templates/ - Custom templates for user-related pages (login, logout, etc.).
	•	static/ - Static files (CSS, JS) for styling the pages.
	•	settings.py - Configuration for enabling HTTPS, disabling social login, and general settings.

Security

	•	HTTPS by default: All connections are forced to be secured with HTTPS.
	•	Password management: Includes password reset functionality with email.
	•	CSRF protection: CSRF tokens are used for all forms to prevent cross-site request forgery.

Requirements

	•	Python 3.10+
	•	Django 4.x
	•	SSL certificate for HTTPS (for production)

Usage

	•	Visit /accounts/login/ to log in.
	•	Visit /accounts/signup/ to register a new user.
	•	Use the admin panel for managing users: /admin/.
