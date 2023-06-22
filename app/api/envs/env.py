# Importing the os module to access environment variables
import os 
# Fetching the values of the environment variables using the os module
MONGO_CLIENT = os.getenv('MONGO_CLIENT')