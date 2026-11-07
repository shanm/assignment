import requests

class ServiceNowClient:
    def __init__(self, instance_url, username, password):
        self.instance_url = f"https://{instance_url}.service-now.com/api/now/table/incident"
        self.auth = (username, password)

    def get_incident(self, incident_id):
        # Logic to retrieve an incident from ServiceNow using the API
        pass

    def create_incident(self, payload):
        # Logic to create a new incident in ServiceNow using the API
        response = requests.post(f"{self.instance_url}", auth=self.auth, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response from ServiceNow

    def update_incident(self, incident_id, updates):
        # Logic to update an existing incident in ServiceNow using the API
        pass

    def delete_incident(self, incident_id):
        # Logic to delete an incident from ServiceNow using the API
        pass
    
client = ServiceNowClient(instance_url="your_instance", username="your_username", password="your_password")

client.create_incident(payload={
    "short_description": "Test incident from FastAPI",
    "description": "This is a test incident created from FastAPI application",
    "urgency": "2",
    "impact": "2"
})