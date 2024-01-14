import requests

# Replace with your actual server URL
base_url = "http://localhost:3000"

# Test ping endpoint
response = requests.get(f"{base_url}/ping/")
print("Ping:", response.text)

# Test pingdb endpoint
response = requests.get(f"{base_url}/pingdb/")
print("PingDB:", response.text)

# Test add_user_to_project endpoint
user_project_data = {"user_email": "user@example.com", "project_pid": "123"}
response = requests.post(f"{base_url}/add_user_to_project", json=user_project_data)
print("Add User to Project:", response.json())

# Test delete_user_from_project endpoint
response = requests.post(f"{base_url}/delete_user_from_project", json=user_project_data)
print("Delete User from Project:", response.json())

# Test add_user_to_task endpoint
user_task_data = {"user_email": "user@example.com", "task_name": "Task1"}
response = requests.post(f"{base_url}/add_user_to_task", json=user_task_data)
print("Add User to Task:", response.json())

# Test delete_user_from_task endpoint
response = requests.post(f"{base_url}/delete_user_from_task", json=user_task_data)
print("Delete User from Task:", response.json())

# Test add_task_to_project endpoint
task_project_data = {"task_name": "Task1", "project_pid": "123"}
response = requests.post(f"{base_url}/add_task_to_project", json=task_project_data)
print("Add Task to Project:", response.json())

# Test create_project endpoint
project_data = {"Pid": "123", "Name": "Project1", "Pm’s": ["pm@example.com"], "Employees": ["user@example.com"]}
response = requests.post(f"{base_url}/create_project", json=project_data)
print("Create Project:", response.json())

# Test create_user endpoint
user_data = {"Email": "user@example.com", "Bool": True, "File": "/path/to/file"}
response = requests.post(f"{base_url}/create_user", json=user_data)
print("Create User:", response.json())

# Test create_task endpoint
task_data = {"Parent proj": "Project1", "Name": "Task1", "Desc": "Task description", "Urgency": "High",
             "Assigned to": "user@example.com", "Date_made": "2024-01-13", "Status": "Pending"}
response = requests.post(f"{base_url}/create_task", json=task_data)
print("Create Task:", response.json())

# Test user_tasks endpoint
response = requests.get(f"{base_url}/user_tasks/user@example.com")
print("User Tasks:", response.json())

# Test promote_to_project_manager endpoint
promote_data = {"user_email": "user@example.com", "project_pid": "123"}
response = requests.post(f"{base_url}/promote_to_project_manager", json=promote_data)
print("Promote User to Project Manager:", response.json())
