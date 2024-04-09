import os
import requests
from helpers.db import fetch_document
import json
url = f"http://{os.environ.get("host")}:8080/api/tasks"

def headers(userId) :
    result = fetch_document(userId)
    return {'Authorization': f"Bearer {result["token"]}"}

def request_body(payload):
    request_body = {}
    request_body["title"] = payload["create_task_title"]["text"]["value"]
    request_body["description"] = payload["create_task_description"]["text"]["value"]
    request_body["status"] = payload["create_task_actions"]["status-select-action"]["selected_option"]["value"]
    # request_body["assignee"] = payload["create_task_actions"]["assignee-select"]["selected_user"]
    request_body["dueDate"] = payload["create_task_actions"]["date-select"]["selected_date"]
    return request_body

def service_create_task(payload, userId):
    payload = request_body(payload)
    try:
        response = requests.post(url, json=payload, headers=headers(userId))
        if response.status_code == 201:
            print("Created task successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_get_tasks(userId):
    try:
        response = requests.get(f"{url}?assignee={userId}", headers=headers(userId))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_update_task(task_id, payload, userId):
    payload = request_body(payload)
    try:
        response = requests.put(f"{url}/{task_id}", headers=headers(userId), json=payload)
        if response.status_code == 200:
            print("Updated task successfully!")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_get_task(task_id, userId):
    try:
        response = requests.get(f"{url}/{task_id}", headers=headers(userId))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_delete_task(task_id, userId):
    try:
        response = requests.delete(f"{url}/{task_id}", headers=headers(userId))
        if response.status_code == 200:
            print("Deleted task successfully!")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def service_login(userId, password):
    try:
        response = requests.post(f"http://{os.environ.get('host')}:8080/api/login", json={"username": userId, "password": password})
        if response.status_code == 200:
            print("Login Success")
            return response.json()
        else:
            raise ValueError(f"Request failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
