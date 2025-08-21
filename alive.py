from astrapy import DataAPIClient

endpoint = os.environ.get("ASTRA_API_ENDPOINT")
token = os.environ.get("ASTRA_AUTH_TOKEN")
keyspace = os.environ.get("KEYSPACE")

client = DataAPIClient(token)
db = client.get_database_by_api_endpoint(endpoint, keyspace=keyspace)
collections = db.list_collection_names()
print(f"Connected successfully. Collections: {collections}")
