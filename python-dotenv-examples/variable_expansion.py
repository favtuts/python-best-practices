import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the value
db_url = os.getenv("DB_URL")

# Print the value
print(f"DB_URL = {db_url}")
