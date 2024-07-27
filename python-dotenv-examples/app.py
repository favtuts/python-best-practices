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


# Get environment variables as a Dictionary
ev = dict(os.environ)

# Print the values from dictionary
print(f"API_KEY = {ev['API_KEY']}")
print(f"DATABASE_URL = {ev['DATABASE_URL']}")
print(f"SECRET = {ev['SECRET_KEY']}")
