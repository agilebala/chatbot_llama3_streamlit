import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()  # Ensure environment variables are loaded

endpoint = os.getenv("COSMOS_ENDPOINT")
key = os.getenv("COSMOS_KEY")

print("Testing Cosmos DB connection...")
try:
    client = CosmosClient(endpoint, key)
    dbs = list(client.list_databases())
    print("✅ Connected! Databases:", [db['id'] for db in dbs])
except Exception as e:
    print("❌ Could not connect to Cosmos DB:", e)
