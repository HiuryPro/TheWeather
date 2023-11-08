from django.db.backends.base.base import BaseDatabaseWrapper
import requests


class MongoDBAtlasAPIBackend(BaseDatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = (
            "jtg3PBsJB8tkQkkzToXEh4nYsU2ggBUfIDkqR1f73p4ijpiau288lLrGY8XYHUMF"
        )
        self.api_url = (
            "https://sa-east-1.aws.data.mongodb-api.com/app/data-ulzvz/endpoint/data/v1"
        )
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def connect(self):
        self.connection = None  # No connection is required for API

    def execute_query(self, query):
        url = f"{self.api_url}/YOUR_MONGODB_CLUSTER_GROUP_ID/databases/YOUR_DATABASE_NAME/collections/YOUR_COLLECTION_NAME/documents"
        response = requests.post(url, headers=self.headers, json=query)
        return response.json()
