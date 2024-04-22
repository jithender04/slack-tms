import os
import requests
from helpers.db import fetch_document
import json
url = f"http://{os.environ.get("host")}:8080/api"


def headers(userId) :
    result = fetch_document(userId)
    if result and "token" in result:
        return {'Authorization': f"Bearer {result["token"]}"}
    else:
        return None

def request_body(payload):
    request_body = {}
    request_body["title"] = payload["create_task_title"]["text"]["value"]
    request_body["description"] = payload["create_task_description"]["text"]["value"]
    request_body["status"] = payload["create_task_actions"]["status-select-action"]["selected_option"]["value"]
    request_body["dueDate"] = payload["create_task_actions"]["date-select"]["selected_date"]
    if "create_task_assignee" in payload:
        request_body["assignee"] = payload["create_task_assignee"]["assignee-select"]["selected_user"]
    return request_body

def service_create_task(payload, userId, data = None):
    payload = request_body(payload)
    try:
        if data and "channel_id" in data:
            payload["channel_id"] = data["channel_id"]
            response = requests.post(f"{url}/{data['channel_id']}/tasks", json=payload, headers=headers(userId))
        else: 
            response = requests.post(f"{url}/tasks", json=payload, headers=headers(userId))
        if response.status_code == 201:
            print("Created task successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_get_tasks(userId):
    try:
        response = requests.get(f"{url}/tasks?assignee={userId}", headers=headers(userId))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_update_task(task_id, payload, userId):
    payload = request_body(payload)
    try:
        response = requests.put(f"{url}/tasks/{task_id}", headers=headers(userId), json=payload)
        if response.status_code == 200:
            print("Updated task successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_get_task(task_id, userId):
    try:
        response = requests.get(f"{url}/tasks/{task_id}", headers=headers(userId))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_delete_task(task_id, userId):
    try:
        response = requests.delete(f"{url}/tasks/{task_id}", headers=headers(userId))
        if response.status_code == 200:
            print("Deleted task successfully!")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_login(userId, password):
    try:
        response = requests.post(f"{url}/login", json={"username": userId, "password": password})
        if response.status_code == 200:
            print("Login Success")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_create_project(payload, userId):
    try:
        response = requests.post(f"{url}/projects", json=payload, headers=headers(userId))
        if response.status_code == 201:
            print("Created project successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_update_project(channel_id, payload, userId):
    try:
        response = requests.put(f"{url}/projects/{channel_id}", headers=headers(userId), json=payload)
        if response.status_code == 200:
            print("Updated project successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_create_account(payload):
    print(payload)
    try:
        response = requests.post(f"{url}/register?multiple_users=true", json=payload)
        if response.status_code == 201:
            print("Created accounts successfully!")
            return response.json()
        elif response.status_code == 200:
            print("Accounts already exists!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
