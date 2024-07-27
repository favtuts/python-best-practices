import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ.get("DEBUG")

if DEBUG=="True":
    db="Test Database"
else:
    db="Production Database"

print(db)