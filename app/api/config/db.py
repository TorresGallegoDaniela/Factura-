# Import MongoClient class and MONGO_CLIENT constant from env module
from pymongo import MongoClient
from app.api.envs.env import MONGO_CLIENT

# Connect to MongoDB client
client = MongoClient(MONGO_CLIENT)

# Access the database
db = client['URLFactura']

# If the client is connected, print a success message to the console
if client:
    print('\033[1;32m ******** DATABASE IS CONNECTED *********')
