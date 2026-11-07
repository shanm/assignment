# pip install requests

import requests
import json
import os

INSTANCE = os.environ.get("INSTANCE")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

# Set the request parameters
# Create a new incident
url = f"https://{INSTANCE}.service-now.com/api/now/table/incident"

payload = {
    "short_description": "Test incident from FastAPI",
    "description": "This is a test incident created from FastAPI application",
    "urgency": "2",
    "impact": "2"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

auth = (USERNAME, PASSWORD)

response = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload), timeout=10)

response.raise_for_status()  # Raise an exception for HTTP errors

print("Incident created successfully!")
print("Response:", response.json())

###################################
# Get an incident
incident_number = "INC0010001"  # Replace with the actual incident number you want to retrieve
url = f"https://{INSTANCE}.service-now.com/api/now/table/incident?sysparm_query=number={incident_number}"

response = requests.get(url, auth=auth, headers=headers)
response.raise_for_status()
print("Incident retrieved successfully!")
print("Response:", response.json())

##################################
# Update an incident
incident_sys_id = "1234567890abcdef1234567890abcdef"  # Replace with the actual sys_id of the incident you want to update
url = f"https://{INSTANCE}.service-now.com/api/now/table/incident/{incident_sys_id}"

payload = {
    "short_description": "Updated test incident from FastAPI",
    "description": "This is an updated test incident created from FastAPI application"
}

response = requests.put(url, auth=auth, headers=headers, data=json.dumps(payload))
response.raise_for_status()
print("Incident updated successfully!")
print("Response:", response.json())