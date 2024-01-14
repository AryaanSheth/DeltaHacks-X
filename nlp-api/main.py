import json
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
creds = redis.UsernamePasswordCredentialProvider("default", "cHCswCCH3MZIn2xB4jxYuyWfLIu0jitD")
r = redis.Redis(
    host='redis-13955.c325.us-east-1-4.ec2.cloud.redislabs.com',
    port=13955,
    decode_responses=True,
    credential_provider=creds
)

import json
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
creds = redis.UsernamePasswordCredentialProvider("default", "cHCswCCH3MZIn2xB4jxYuyWfLIu0jitD")
r = redis.Redis(
    host='redis-13955.c325.us-east-1-4.ec2.cloud.redislabs.com',
    port=13955,
    decode_responses=True,
    credential_provider=creds
)

@app.route('/ping/', methods=['GET', 'POST'])
def welcome():
    return "pong"

@app.route('/pingdb/', methods=['GET', 'POST'])
def pingdb():
    return str(r.ping())

# Example to store user data
def store_user(user_data):
    email = user_data['Email']
    is_pm = user_data['Bool']
    file_path = user_data['File']
    
    user_key = f'user:{email}'
    
    r.hset(user_key, 'Bool', is_pm)
    r.hset(user_key, 'Email', email)
    r.hset(user_key, 'File', file_path)

# Example to store project data
def store_project(project_data):
    pid = project_data['Pid']
    name = project_data['Name']
    pm_emails = project_data['Pm’s']
    employee_emails = project_data['Employees']
    
    project_key = f'project:{pid}'
    
    r.hset(project_key, 'Pid', pid)
    r.hset(project_key, 'Name', name)
    r.sadd(f'{project_key}:pm_emails', *pm_emails)
    r.sadd(f'{project_key}:employee_emails', *employee_emails)

# Example to store task data
def store_task(task_data):
    parent_proj = task_data['Parent proj']
    name = task_data['Name']
    desc = task_data['Desc']
    urgency = task_data['Urgency']
    assigned_to = task_data['Assigned to']
    date_made = task_data['Date_made']
    status = task_data['Status']
    
    task_key = f'task:{name}'
    
    r.hset(task_key, 'Parent proj', parent_proj)
    r.hset(task_key, 'Name', name)
    r.hset(task_key, 'Desc', desc)
    r.hset(task_key, 'Urgency', urgency)
    r.hset(task_key, 'Assigned to', assigned_to)
    r.hset(task_key, 'Date_made', date_made)
    r.hset(task_key, 'Status', status)

# Add user to project
@app.route('/add_user_to_project', methods=['POST'])
def add_user_to_project():
    try:
        data = request.json
        user_email = data.get('user_email')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.sadd(f'{project_key}:employee_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User added to project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Delete user from project
@app.route('/delete_user_from_project', methods=['POST'])
def delete_user_from_project():
    try:
        data = request.json
        user_email = data.get('user_email')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.srem(f'{project_key}:employee_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User deleted from project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Add user to task
@app.route('/add_user_to_task', methods=['POST'])
def add_user_to_task():
    try:
        data = request.json
        user_email = data.get('user_email')
        task_name = data.get('task_name')
        
        task_key = f'task:{task_name}'
        r.hset(task_key, 'Assigned to', user_email)
        
        return jsonify({'status': 'success', 'message': 'User added to task successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Delete user from task
@app.route('/delete_user_from_task', methods=['POST'])
def delete_user_from_task():
    try:
        data = request.json
        user_email = data.get('user_email')
        task_name = data.get('task_name')
        
        task_key = f'task:{task_name}'
        r.hdel(task_key, 'Assigned to')
        
        return jsonify({'status': 'success', 'message': 'User deleted from task successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Add task to project
@app.route('/add_task_to_project', methods=['POST'])
def add_task_to_project():
    try:
        data = request.json
        task_name = data.get('task_name')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.sadd(f'{project_key}:tasks', task_name)
        
        return jsonify({'status': 'success', 'message': 'Task added to project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Create project
@app.route('/create_project', methods=['POST'])
def create_project():
    try:
        data = request.json
        store_project(data)
        
        return jsonify({'status': 'success', 'message': 'Project created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Create user
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.json
        store_user(data)
        
        return jsonify({'status': 'success', 'message': 'User created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Create task
@app.route('/create_task', methods=['POST'])
def create_task():
    try:
        data = request.json
        store_task(data)
        
        return jsonify({'status': 'success', 'message': 'Task created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# List tasks a user is working on
@app.route('/user_tasks/<user_email>', methods=['GET'])
def user_tasks(user_email):
    tasks = []
    for task_key in r.scan_iter('task:*'):
        task_data = r.hgetall(task_key)
        if task_data.get('Assigned to') == user_email:
            tasks.append(task_data)

    return jsonify(tasks)

@app.route('/promote_to_project_manager', methods=['POST'])
def promote_to_project_manager():
    try:
        data = request.json
        user_email = data.get('user_email')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.sadd(f'{project_key}:pm_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User promoted to project manager successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=3000)
