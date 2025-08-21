from astrapy import DataAPIClient

ASTRA_API_ENDPOINT = os.environ.get("ASTRA_API_ENDPOINT")
AUTH_TOKEN = os.environ.get("ASTRA_AUTH_TOKEN")
keyspace = os.environ.get("default_keyspace")

client = DataAPIClient(token)
db = client.get_database_by_api_endpoint(endpoint, keyspace=keyspace)
collections = db.list_collection_names()
print(f"Connected successfully. Collections: {collections}")
