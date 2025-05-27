import os
from azure.cosmos import CosmosClient, PartitionKey
from .config import COSMOS_ENDPOINT, COSMOS_KEY, COSMOS_CONTAINER, COSMOS_DATABASE

class CosmosDB:
    def __init__(self):
        self.client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        self.database = self.client.create_database_if_not_exists(id=COSMOS_DATABASE)
        self.container = self.database.create_container_if_not_exists(
            id=COSMOS_CONTAINER,
            partition_key=PartitionKey(path="/session_id"),
            offer_throughput=400
        )

    def save_message(self, session_id, role, message):
        self.container.upsert_item({
            "id": f"{session_id}-{role}-{len(message)}",
            "session_id": session_id,
            "role": role,
            "message": message
        })

    def get_conversation(self, session_id):
        query = (
            "SELECT * FROM c WHERE c.session_id=@session_id ORDER BY c._ts ASC"
        )
        items = list(self.container.query_items(
            query=query,
            parameters=[{"name": "@session_id", "value": session_id}],
            enable_cross_partition_query=True
        ))
        return [(item["role"], item["message"]) for item in items]
