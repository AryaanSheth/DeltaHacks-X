import requests

# Replace with your actual server URL
base_url = "http://localhost:3000"

# Test ping endpoint
response = requests.get(f"{base_url}/ping/")
assert response.text == "pong"

# Test pingdb endpoint
response = requests.get(f"{base_url}/pingdb/")
assert response.text == "True"

# Test add_user_to_project endpoint
user_project_data = {"user_email": "user@example.com", "project_pid": "123"}
response = requests.post(f"{base_url}/add_user_to_project", json=user_project_data)
assert response.json() == {'status': 'success', 'message': 'User added to project successfully'}

# Test delete_user_from_project endpoint
response = requests.post(f"{base_url}/delete_user_from_project", json=user_project_data)
assert response.json() == {'status': 'success', 'message': 'User deleted from project successfully'}

# Test add_user_to_task endpoint
user_task_data = {"user_email": "user@example.com", "task_name": "Task1"}
response = requests.post(f"{base_url}/add_user_to_task", json=user_task_data)
assert response.json() == {'status': 'success', 'message': 'User added to task successfully'}

# Test delete_user_from_task endpoint
response = requests.post(f"{base_url}/delete_user_from_task", json=user_task_data)
assert response.json() == {'status': 'success', 'message': 'User deleted from task successfully'}

# Test add_task_to_project endpoint
task_project_data = {"task_name": "Task1", "project_pid": "123"}
response = requests.post(f"{base_url}/add_task_to_project", json=task_project_data)
assert response.json() == {'status': 'success', 'message': 'Task added to project successfully'}

# Test create_project endpoint
project_data = {"Pid": "123", "Name": "Project1", "Pm’s": ["pm@example.com"], "Employees": ["user@example.com"]}
response = requests.post(f"{base_url}/create_project", json=project_data)
assert response.json() == {'status': 'success', 'message': 'Project created successfully'}

# Test create_user endpoint
user_data = {"Email": "user@example.com", "Bool": True, "File": "/path/to/file"}
response = requests.post(f"{base_url}/create_user", json=user_data)
assert response.json() == {'status': 'success', 'message': 'User created successfully'}

# Test create_task endpoint
task_data = {"Parent proj": "Project1", "Name": "Task1", "Desc": "Task description", "Urgency": "High",
             "Assigned to": "user@example.com", "Date_made": "2024-01-13", "Status": "Pending"}
response = requests.post(f"{base_url}/create_task", json=task_data)
assert response.json() == {'status': 'success', 'message': 'Task created successfully'}

# Test user_tasks endpoint
response = requests.get(f"{base_url}/user_tasks/user@example.com")
assert isinstance(response.json(), list)

# Test delete_task_from_project endpoint
response = requests.post(f"{base_url}/delete_task_from_project", json=task_project_data)
assert response.json() == {'status': 'success', 'message': 'Task deleted from project successfully'}

# Test delete_user endpoint
delete_user_data = {"user_email": "user@example.com"}
response = requests.post(f"{base_url}/delete_user", json=delete_user_data)
assert response.json() == {'status': 'success', 'message': 'User deleted successfully'}

# Test delete_project endpoint
delete_project_data = {"project_pid": "123"}
response = requests.post(f"{base_url}/delete_project", json=delete_project_data)
assert response.json() == {'status': 'success', 'message': 'Project deleted successfully'}

# Test update_task_status endpoint
update_task_status_data = {"task_name": "Task1", "new_status": "Completed"}
response = requests.post(f"{base_url}/update_task_status", json=update_task_status_data)
assert response.json() == {'status': 'success', 'message': 'Task status updated successfully'}

# Test demote_user endpoint
demote_user_data = {"user_email": "user@example.com", "project_pid": "123"}
response = requests.post(f"{base_url}/demote_user", json=demote_user_data)
assert response.json() == {'status': 'success', 'message': 'User demoted successfully'}

print("All tests passed!")
