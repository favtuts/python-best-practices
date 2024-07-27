# Python Dotenv: How To Manage Environment Variables in Python
* https://tuts.heomi.net/python-dotenv-how-to-manage-environment-variables-in-python/
* https://tuts.heomi.net/using-env-files-for-environment-variables-in-python-applications/

# Preparing the Python environment

We are using Python3.10
```sh
$ python3 --version
Python 3.10.14
$ pip install --upgrade pip
```

Install Pipenv 
```sh
$ cd python-dotenv-examples
~/python-dotenv-examples$ pip install pipenv
```

Use pipenv to start our project and manage our dependencies
```sh
$ pipenv --python 3.10
Creating a virtualenv for this project...
Pipfile: /home/tvt/techspace/python/python-best-practices/python-dotenv-examples/Pipfile
Using /home/tvt/.pyenv/versions/3.10.14/bin/python (3.10.14) to create virtualenv...
⠏ Creating virtual environment...created virtual environment CPython3.10.14.final.0-64 in 1194ms
  creator CPython3Posix(dest=/home/tvt/.local/share/virtualenvs/python-dotenv-examples-9VBF62Vw, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/tvt/.local/share/virtualenv)
    added seed packages: pip==24.1, setuptools==70.1.0, wheel==0.43.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/tvt/.local/share/virtualenvs/python-dotenv-examples-9VBF62Vw
Creating a Pipfile for this project...
```

Activate the environment
```sh
$ pipenv shell
(python-dotenv-examples) $ python --version
Python 3.10.14
```

# Getting Started with Python Dotenv

## Installation python-dotenv library
```sh
(python-dotenv-examples) $ pipenv install python-dotenv
```

## Setting up the .env File

```sh
(python-dotenv-examples) $ touch .env
```

Example key-value pairs
```ini
API_KEY=abcd1234ef56
DATABASE_URL=mydatabase://123
SECRET_KEY=secret
```

# Loading Environment Variables with Python Dotenv

## Basic Setup with load_dotenv()

Create a new Python file named `app.py` 
```sh
(python-dotenv-examples) $ touch app.py
```

with following snippet:
```python
import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the values
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
secret = os.getenv("SECRET_KEY")

# Print the values
print(f"API_KEY = {api_key}")
print(f"DATABASE_URL = {database_url}")
print(f"SECRET = {secret}")
```

Open this [app.py](app.py) file in VSCode and sellect Python interpreter `python-dotenv-examples-9VBF62Vw`.

Run this file to see the results
```sh
(python-dotenv-examples) $ python app.py

API_KEY = abcd1234ef56
DATABASE_URL = mydatabase://123
SECRET = secret
```

## Loading Environment Variables as a Dictionary

The above example require you are working with many variables. to avoid that, we can load all values into single dictionary, and extract them from that.
```python
# Get environment variables as a Dictionary
ev = dict(os.environ)

# Print the values from dictionary
print(f"API_KEY = {ev['API_KEY']}")
print(f"DATABASE_URL = {ev['DATABASE_URL']}")
print(f"SECRET = {ev['SECRET_KEY']}")
```

# Managing Variables in Different Environments

Add the bellow contents to `.env` file
```ini
DEV_DB_USER="user_dev"
DEV_DB_PASS="pass_dev"
PROD_DB_USER="user_prod"
PROD_DB_PASS="pass_prod"
```

Create new Python file [environments.py](environments.py):
```python
import os
import platform
from dotenv import load_dotenv

# Detect platform to set the environment
environ = "PROD" if platform.system().lower() == "linux" else "DEV"

# Load the stored environment variables
load_dotenv()

# Get the values
db_user = os.getenv(f"{environ}_DB_USER")
db_pass = os.getenv(f"{environ}_DB_PASS")

# Print the values
print(f"USER = {db_user}")
print(f"PASS = {db_pass}")
```
By doing so, you can make a distinction:
* If Linux, it’s a production environment
* Else, it’s a development environment

Run this scrip on Linux OS to see the results
```sh
(python-dotenv-examples) $ python environments.py 
platform=Linux
USER = user_prod
PASS = pass_prod
```

# Advanced Python Dotenv Variable Expansions

Python dotenv supports variable expansion, which is a helpful feature when dealing with multiline values or referencing pre-existing environment variables
```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database
DB_URL=jdbc:postgresql://${DB_HOST}:${DB_PORT}/${DB_NAME}
```

You can now grab only `DB_URL` which will automatically reference the other three environment variables:
```python
import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the value
db_url = os.getenv("DB_URL")

# Print the value
print(f"DB_URL = {db_url}")
```

This is the output you will see:
```sh
(python-dotenv-examples) $ python variable_expansion.py 
DB_URL = jdbc:postgresql://localhost:5432/database
```

# Using Python Dotenv CLI Interface

```sh
(python-dotenv-examples) $ dotenv list
It seems python-dotenv is not installed with cli option. 
Run pip install "python-dotenv[cli]" to fix this.
```

Fixed:
```sh
(python-dotenv-examples) $ pipenv install "python-dotenv[cli]"
```

Now you can list all variables
```sh
(python-dotenv-examples) $ dotenv list
API_KEY=abcd1234ef56
DATABASE_URL=mydatabase://123
DB_HOST=localhost
DB_NAME=database
DB_PORT=5432
DB_URL=jdbc:postgresql://localhost:5432/database
```

You can set new variable
```sh
(python-dotenv-examples) $ dotenv set DB_USER mark123

DB_USER=mark123
```

# Use .env as application settings

Create new file `gcp.env` to store GCP project settings
```ini
# environment variables defined inside a .env file
GCP_PROJECT_ID=my-project-id
SERVICE_ACCOUNT_FILE=path/to/serviceAccountCredentials
STORAGE_BUCKET_NAME=my-super-important-data
```

By default `load_dotenv` will look for the .env file in the current working directory or any parent directories however you can also specify the path if your particular use case requires it be stored elsewhere. 

Create a `settings.py` file:
```python
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
```

Create a `gcp_app.py` file
```python
import settings as gcp_config

print(f"ProjectID  = {gcp_config.GCP_PROJECT_ID}")
```
Run to see the results:
```sh
(python-dotenv-examples) $ python gcp_app.py 
ProjectID  = my-project-id
```

# Using .env file for Configuration switching

In the `.env` file, add the variable:
```ini
DEBUG=True
```

Create the `switch_configuration.py` file
```python
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ.get("DEBUG")

if DEBUG=="True":
    db="Test Database"
else:
    db="Production Database"

print(db)
```

Test for the result
```sh
(python-dotenv-examples) $ python switch_configuration.py 
Test Database
```

You can change to Production configuration
```ini
DEBUG=False
```

Test for the result
```sh
(python-dotenv-examples) $ python switch_configuration.py 
Production Database
```