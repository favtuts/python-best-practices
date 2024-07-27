import os
import platform
from dotenv import load_dotenv

# Detect platform to set the environment
print(f"platform={platform.system()}")
environ = "PROD" if platform.system().lower() == "linux" else "DEV"

# Load the stored environment variables
load_dotenv()

# Get the values
db_user = os.getenv(f"{environ}_DB_USER")
db_pass = os.getenv(f"{environ}_DB_PASS")

# Print the values
print(f"USER = {db_user}")
print(f"PASS = {db_pass}")