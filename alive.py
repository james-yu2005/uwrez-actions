import os
from astrapy import DataAPIClient

# Get credentials from environment variables
token = os.getenv('DB_TOKEN')
endpoint = os.getenv('DB_ENDPOINT')
keyspace = os.getenv('DB_KEYSPACE')

# Validate that all required environment variables are set
if not all([token, endpoint, keyspace]):
    missing = []
    if not token: missing.append('DB_TOKEN')
    if not endpoint: missing.append('DB_ENDPOINT')
    if not keyspace: missing.append('DB_KEYSPACE')
    raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

try:
    client = DataAPIClient(token)
    db = client.get_database_by_api_endpoint(endpoint, keyspace=keyspace)
    collections = db.list_collection_names()
    print(f"✅ Connected successfully. Collections: {collections}")
    print(f"Database endpoint: {endpoint}")
    print(f"Keyspace: {keyspace}")
    print(f"Number of collections: {len(collections)}")
except Exception as e:
    print(f"❌ Connection failed: {str(e)}")
    exit(1)
