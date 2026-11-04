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

**13.** Dependency Information

**14.** Application Highlights

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
    "password_text": "test"
    "password_strength": 0
    "password_attributes": {
        "length": 4,
        "uppercase": 0,
        "lowercase": 4,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 1,
        "previous_password": 0,
        "contains_personal_information": 0,
        "variety_of_characters": 0,
    }
    "password_strengths": ["The password contains at least 1 lowercase letter (a-z)", "The password is new and has not been used previously", "The password does not contain personal information (username, date of birth, etc.)"]
    "password_weaknesses": ["The password is too short (less than 10 characters)", "The password does not contain any uppercase letters (A-Z)", "The password does not contain any numbers (0-9)", "The password does not contain any special characters (!, @, #, etc.)", "The password contains 1 or more common words or phrases", "The password does not contain a large variety of uppercase letters, lowercase letters, numbers, and special characters", "The password does not contain a large variety of characters"]
}
```

### Password 2

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": "TestP@ssword123!"
    "password_strength": 78
    "password_attributes": {
        "length": 16,
        "uppercase": 2,
        "lowercase": 9,
        "numbers": 3,
        "special_characters": 2,
        "contains_common_words": 1,
        "previous_password": 1,
        "contains_personal_information": 0,
        "variety_of_characters": 1,
    }
    "password_strengths": ["The password is of sufficient length (10 characters or longer)", "The password contains at least 1 uppercase letter (A-Z)", "The password contains at least 1 lowercase letter (a-z)", "The password contains at least 1 number (0-9)", "The password contains at least 1 special character (!, @, #, etc.)", "The password does not contain personal information (username, date of birth, etc.)", "The password contains a large variety of uppercase letters, lowercase letters, numbers, and special characters", "The password contains a large variety of characters"]
    "password_weaknesses": ["The password could be longer (up to 30 characters)", "The password contains 1 or more common words or phrases", "The password has been used previously"]
}
```

### Password 3

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    "password_strength": 30
    "password_attributes": {
        "length": 30,
        "uppercase": 0,
        "lowercase": 30,
        "numbers": 0,
        "special_characters": 0,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 1,
        "variety_of_characters": 0,
    }
    "password_strengths": ["The password is of sufficient length (10 characters or longer)", "The password contains at least 1 lowercase letter (a-z)", "The password does not contain common words or phrases", "The password is new and has not been used previously"]
    "password_weaknesses": ["The password does not contain any uppercase letters (A-Z)", "The password does not contain any numbers (0-9)", "The password does not contain any special characters (!, @, #, etc.)", "The password contains 1 or more pieces of personal information (username, date of birth, etc.)", "The password does not contain a large variety of uppercase letters, lowercase letters, numbers, and special characters", "The password does not contain a large variety of characters"]
}
```

### Password 4

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": 1!Aaaaaaaaaaaaaaaaaaaaaaaaaaaa
    "password_strength": 46
    "password_attributes": {
        "length": 30,
        "uppercase": 1,
        "lowercase": 27,
        "numbers": 1,
        "special_characters": 1,
        "contains_common_words": 1,
        "previous_password": 0,
        "contains_personal_information": 0,
        "variety_of_characters": 0,
    }
    "password_strengths": ["The password is of sufficient length (10 characters or longer)", "The password contains at least 1 uppercase letter (A-Z)", "The password contains at least 1 lowercase letter (a-z)", "The password contains at least 1 number (0-9)", "The password contains at least 1 special character (!, @, #, etc.)", "The password is new and has not been used previously", "The password does not contain personal information (username, date of birth, etc.)"]
    "password_weaknesses": ["The password contains 1 or more common words or phrases", "The password contains a large variety of uppercase letters, lowercase letters, numbers, and special characters", "The password does not contain a large variety of characters"]
}
```

### Password 5

```
"model": "PasswordCheck.Password"
"fields": {
    "password_text": hS56Dw@u#U67^*Jgt2*$Jj4A!u9W1P
    "password_strength": 100
    "password_attributes": {
        "length": 30,
        "uppercase": 8,
        "lowercase": 7,
        "numbers": 8,
        "special_characters": 7,
        "contains_common_words": 0,
        "previous_password": 0,
        "contains_personal_information": 0,
        "variety_of_characters": 1,
    }
    "password_strengths": ["The password is of sufficient length (10 characters or longer)", "The password contains at least 1 uppercase letter (A-Z)", "The password contains at least 1 lowercase letter (a-z)", "The password contains at least 1 number (0-9)", "The password contains at least 1 special character (!, @, #, etc.)", "The password does not contain common words or phrases", "The password is new and has not been used previously", "The password does not contain personal information (username, date of birth, etc.)", "The password contains a large variety of uppercase letters, lowercase letters, numbers, and special characters", "The password contains a large variety of characters"]
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

2. **Pull Changes**
    - Before committing, in Bash, type `git pull`
    - This will ensure that all changes are accounted for before committing

3. **Commit to the New Branch**
    - In Bash, type `git add *` to add the files for the commit
    - In Bash, type `git commit -m "<message>"` to make the commit

4. **Push Changes**
    - In Bash, type `git push --set-upstream origin <branch_name>`
    - This will push all changes made

5. **Make a Pull Request**
    - Go to the `Password-Checker` repository and click on the `Pull requests` tab
    - Click on `New pull request`. Click the `compare` dropdown and select the appropriate Git branch. Click `Create pull request`
    - Enter the appropriate information and click `Create pull request`

6. **Wait for the Pull Request to be Accepted**
    - Wait for someone to accept the pull request and merge the changes
    - Once the pull request has been accepted, in Bash, type `git checkout main` and `git pull`
    - This will switch to the main branch and pull the latest changes.

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

## 13. Dependency Information

- Django: Python web framework used to create this application
- PyInstaller: Bundles this application and its dependencies into a single package
- pyinstaller-hooks-contrib: Automatically installed alongside PyInstaller

## 14. Application Highlights

- Ability to quickly enter passwords and get immediate in-depth feedback
- In-depth evaluation and calculation of password strength
- Hidden passwords which are never shown in plain text or saved within the application
- Modern web architecture (Django + Bootstrap)
- Open-source code that is easy to extend and customize

## 15. Video Demonstration

