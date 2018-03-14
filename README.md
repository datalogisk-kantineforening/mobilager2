# Mobilager
This is a project made for keeping track of the inventory at
[Datalogisk Kantineforening](https://kantinen.org)

## Setup
To install you need to install the packages in `requirements.txt`. It is not
required but it's recommended to set up a virtualenv

- Install the required packages with `pip install -r requirements.txt`
- For development set the environment variable `DJANGO_ENV="DEV"`
(on UNIX like systems run `export DJANGO_ENV=DEV`)
- Run the migrations `python manage.py migrate`
- Load the test database `python manage.py loaddata fixtures/EventType.json`
- Create a user by running `python manage.py createsuperuser`
- Create a file called `users.auth.php` which contains the users in the
following format `username:crypt:real name:e-mail:groups`
    - username: The username you used in the previous command
    - real name: Your real name e.g. "John Doe"
    - e-mail: Your e-mail
    - groups: Should be "user"
    - crypt: calculate this by running the following commands in Python:
```Python
from crypt import crypt
crypt(password, password)
```
Use the output from the last command in place of "crypt". Note this should only
be used for development

## Running
If you have followed the instructions in [the setup section](#Setup) you should
be ready to run the server.
- Run `python manage.py runserver`
