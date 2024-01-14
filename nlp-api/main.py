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

# Example route to get user data from Redis
@app.route('/get_user/<email>', methods=['GET'])
def get_user(email):
    user_key = f'user:{email}'
    user_data = r.hgetall(user_key)
    
    return jsonify(user_data)

# Example route to get project data from Redis
@app.route('/get_project/<pid>', methods=['GET'])
def get_project(pid):
    project_key = f'project:{pid}'
    project_data = {
        'Pid': r.hget(project_key, 'Pid'),
        'Name': r.hget(project_key, 'Name'),
        'Pm’s': r.smembers(f'{project_key}:pm_emails'),
        'Employees': r.smembers(f'{project_key}:employee_emails')
    }
    
    return jsonify(project_data)

# Example route to get task data from Redis
@app.route('/get_task/<name>', methods=['GET'])
def get_task(name):
    task_key = f'task:{name}'
    task_data = r.hgetall(task_key)
    
    return jsonify(task_data)

@app.route('/get_tasks/', methods=['GET'])
def get_tasks():
    tasks = []
    for task_key in r.scan_iter('task:*'):
        task_data = r.hgetall(task_key)
        tasks.append(task_data)

    return jsonify(tasks)

# Endpoint to store a task
@app.route('/store_task', methods=['POST'])
def store_task_endpoint():
    try:
        task_data = request.json  # Assuming the data is sent in JSON format in the request body
        store_task(task_data)
        return jsonify({'status': 'success', 'message': 'Task stored successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=3000)
