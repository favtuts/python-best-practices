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
