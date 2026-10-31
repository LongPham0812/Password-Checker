# Password Checker

**Author:** Long Pham

**Description:** This is a simple web application that allows users to input a password and evaluate its strength against a set of criteria. The application will evaluate the strength of the password and provide a list of strengths and weaknesses associated with the password. The application aims to provide a simple and user-friendly platform where users can enter passwords, have them evaluated, and get feedback on them so that they can improve them.

## Table of Contents

**1.** Features

**2.** Requirements

**3.** Setup

**4.** Install Dependencies

**5.** Database Setup

**6.** Additional Setup

**7.** Run Development Server

**8.** Testing

**9.** URLs

**10.** Test Data

**11.** UI Design

**12.** Merging Information

**13.** Additional Dependencies

**14.** System Highlights

**15.** Video Demonstration

## 1. Features

- Home Page
    - Text field for the user to input a password
    - 2 checkboxes for the user if the corresponding statements apply to the password
    - Description of how the web application works
    - List of criteria used to evaluate the strength of the password

- Results Page
    - Number and progress bar indicating the strength of the inputted password
    - List of strengths associated with the password to tell the user what they did right with the password.
    - List of weaknesses associated with the password to provide the user with feedback to improve the password.

## 2. Requirements

- Python (version 3.12 or higher)
- pip

## 3. Setup

**1.** Clone repository by typing `git clone https://github.com/LongPham0812/Password-Checker.git` into the command line.
**2.** `cd Password-Checker`

## 4. Install Dependencies

**1.** `pip install -r requirements.txt` (installs Django and other Python packages)

## 5. Database Setup

The database settings under `PasswordChecker/settings.py` should look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 6. Additional Setup

**1.** In Bash, type `python manage.py makemigrations` (then make sure to set up the database model objects )
**2.** In Bash, type `python manage.py migrate`
**3.** In Bash, type `python manage.py createsuperuser` (makes a superuser)
**4.** When prompted, enter `admin` for the username, `admin@gmail.com` for the email address, and `admin` for the password.

## 7. Run Development Server

**1.** In Bash, type `python manage.py runserver` (runs the app)

## 8. Testing

**1.** In Bash, type `python manage.py test` (runs the tests)

## 9. URLs

- (http://127.0.0.1:8000/admin/) - directs to the Django admin portal for the app
- (http://127.0.0.1:8000/) - redirects to the home page of the app
- (http://127.0.0.1:8000/password_checker/) - directs to the home page of the app
- (http://127.0.0.1:8000/password_checker/check_password/) - directs to the results page (redirects to the home page if no password is entered)

## 10. Test Data

The following test data is used in the unit tests for the Password Checker application. These include sample password data to validate the functionality of models used in the application.

### Password 1

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 
    "password_strength": 
    "password_attributes": {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
    }
    "password_strengths": []
    "password_weaknesses": []
}
```

### Password 2

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 
    "password_strength": 
    "password_attributes": {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
    }
    "password_strengths": []
    "password_weaknesses": []
}
```

### Password 3

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 
    "password_strength": 
    "password_attributes": {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
    }
    "password_strengths": []
    "password_weaknesses": []
}
```

### Password 4

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 
    "password_strength": 
    "password_attributes": {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
    }
    "password_strengths": []
    "password_weaknesses": []
}
```

### Password 5

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 
    "password_strength": 
    "password_attributes": {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
    }
    "password_strengths": []
    "password_weaknesses": []
}
```

## 11. UI Design

Figma UI design for the project: https://www.figma.com/design/3kyZk5Y3HvFQPVGrrW33Yc/Password-Checker?node-id=0-1&t=scRZ8UZ4swCa07E7-1

## 12. Merging Information

### Pre-Merge Information

1. **Check for any pending migrations:**

- In Bash, type `python manage.py showmigrations | grep "\[ \]"`
- If there are pending migrations, you will see output like `[ ]`
- If there are no pending migrations, you will see output like `[X]`
- If there are pending migrations, you can apply them with `python manage.py makemigrations` and `python manage.py migrate`

2. **Run any tests:**

- In Bash, type `python manage.py test`
- This will run the tests and check for any errors

3. **Delete expired sessions:**
    - In Bash, type `python manage.py clearsessions`
    - This will check for any expired sessions and delete them

### Merging Information

1. **Make a New Git Branch:**

    - In Bash, type `git checkout -b <branch_name>`
    - This will create a new Git branch and switch to it

### Post-Merge Information

1. **Pull the latest changes:**
    - In Bash, type `git pull origin main`
    - This will pull the latest changes from the main production branch

2. **Create and apply migrations:**
    - In Bash, type `python manage.py makemigrations`
    - In Bash, type `python manage.py migrate`
    - This will create and apply any migrations that are needed

3. **Delete expired sessions:**
    - In Bash, type `python manage.py clearsessions`
    - This will check for any expired sessions and delete them

## 13. Additional Dependencies



## 14. System Highlights



## 15. Video Demonstration

