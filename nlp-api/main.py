import json
from flask import Flask, request, jsonify
import redis

from nlp import *
from resumeParse import *

app = Flask(__name__)
creds = redis.UsernamePasswordCredentialProvider("", "")
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

@app.route('/', methods=['GET', 'POST'])
def root():
    return "Welcome to the NLP API"

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
    pm_emails = project_data['pm']
    employee_emails = project_data['Employees']
    
    project_key = f'project:{pid}'
    
    r.hset(project_key, 'Pid', pid)
    r.hset(project_key, 'Name', name)
    r.sadd(f'{project_key}:pm_emails', *pm_emails)
    r.sadd(f'{project_key}:employee_emails', *employee_emails)

    print(r.hgetall(project_key))

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

@app.route('/add_user_to_project/<user_email>/<project_pid>/', methods=['POST'])
def add_user_to_project(user_email, project_pid):
    try:
        project_key = f'project:{project_pid}'
        r.sadd(f'{project_key}:employee_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User added to project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Delete user from project
@app.route('/delete_user_from_project/<user_email>/<project_pid>/', methods=['POST'])
def delete_user_from_project(user_email, project_pid):
    try:
        project_key = f'project:{project_pid}'
        r.srem(f'{project_key}:employee_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User deleted from project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


# Add user to task
@app.route('/add_user_to_task/<user_email>/<task_name>/', methods=['POST'])
def add_user_to_task(user_email, task_name):
    try:
        task_key = f'task:{task_name}'
        r.hset(task_key, 'Assigned to', user_email)
        
        return jsonify({'status': 'success', 'message': 'User added to task successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Delete user from task
@app.route('/delete_user_from_task/<user_email>/<task_name>/', methods=['POST'])
def delete_user_from_task(user_email, task_name):
    try:
        task_key = f'task:{task_name}'
        r.hdel(task_key, 'Assigned to')
        
        return jsonify({'status': 'success', 'message': 'User deleted from task successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Add task to project
@app.route('/add_task_to_project/<task_name>/<project_pid>/', methods=['POST'])
def add_task_to_project(task_name, project_pid):
    try:
        project_key = f'project:{project_pid}'
        r.sadd(f'{project_key}:tasks', task_name)
        
        return jsonify({'status': 'success', 'message': 'Task added to project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Update the /create_project route to use URL parameters with GET method
@app.route('/create_project/<pid>/<name>/<pm_email>/<employee_email>/', methods=['GET'])
def create_project(pid, name, pm_email, employee_email):
    try:
        project_data = {
            'Pid': pid,
            'Name': name,
            'pm': [pm_email],  # Replace 'Pm’s' with 'pm'
            'Employees': [employee_email]
        }
        store_project(project_data)

        return jsonify({'status': 'success', 'message': 'Project created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})



# Update the /create_user route to use URL parameters
@app.route('/create_user/<email>/<bool_value>/<file_path>/', methods=['POST'])
def create_user(email, bool_value, file_path):
    try:
        user_data = {
            'Email': email,
            'Bool': bool_value,
            'File': file_path
        }
        store_user(user_data)

        return jsonify({'status': 'success', 'message': 'User created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Update the /create_task route to use URL parameters
@app.route('/create_task/<parent_proj>/<name>/<desc>/<urgency>/<assigned_to>/<date_made>/<status>/', methods=['POST'])
def create_task(parent_proj, name, desc, urgency, assigned_to, date_made, status):
    try:
        task_data = {
            'Parent proj': parent_proj,
            'Name': name,
            'Desc': desc,
            'Urgency': urgency,
            'Assigned to': assigned_to,
            'Date_made': date_made,
            'Status': status
        }
        store_task(task_data)

        return jsonify({'status': 'success', 'message': 'Task created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


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

@app.route('/delete_task_from_project', methods=['POST'])
def delete_task_from_project():
    try:
        data = request.json
        task_name = data.get('task_name')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.srem(f'{project_key}:tasks', task_name)
        
        return jsonify({'status': 'success', 'message': 'Task deleted from project successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        data = request.json
        user_email = data.get('user_email')
        
        user_key = f'user:{user_email}'
        r.delete(user_key)
        
        return jsonify({'status': 'success', 'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/delete_project', methods=['POST'])
def delete_project():
    try:
        data = request.json
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.delete(project_key)
        
        return jsonify({'status': 'success', 'message': 'Project deleted successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/update_task_status', methods=['POST'])
def update_task_status():
    try:
        data = request.json
        task_name = data.get('task_name')
        new_status = data.get('new_status')
        
        task_key = f'task:{task_name}'
        r.hset(task_key, 'Status', new_status)
        
        return jsonify({'status': 'success', 'message': 'Task status updated successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/demote_user', methods=['POST'])
def demote_user():
    try:
        data = request.json
        user_email = data.get('user_email')
        project_pid = data.get('project_pid')
        
        project_key = f'project:{project_pid}'
        r.srem(f'{project_key}:pm_emails', user_email)
        
        return jsonify({'status': 'success', 'message': 'User demoted successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/invite/<pid>/<project_name>', methods=['GET', 'POST'])
def invite_user(pid, project_name):
    try:
        project_key = f'project:{pid}'
        project_data = r.hgetall(project_key)
        # Use the project_name from the URL instead of the JSON payload
        return jsonify({'status': 'success', 'message': f'Project {project_name} has been created'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/user_tasks/<user_email>/', methods=['GET'])
def user_tasks(user_email):
    tasks = []
    for task_key in r.scan_iter('task:*'):
        task_data = r.hgetall(task_key)
        if task_data.get('Assigned to') == user_email:
            tasks.append(task_data)

    return jsonify(tasks)

# Update the /get_projects route to remove the limit parameter
@app.route('/get_projects/', methods=['GET'])
def get_projects():
    try:
        projects = []
        for project_key in r.scan_iter('project:*'):
            if r.type(project_key) == b'hash':
                project_data = r.hgetall(project_key)
                projects.append(project_data)
            elif r.type(project_key) == b'set':
                # Handle set type keys (if necessary)

                pass
            else:
                # Handle other types if needed
                pass

        return jsonify(projects)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/nlp/', methods=['GET'])
def nlp():
    try:
        path = 'nlp-api/resume2.pdf'
        desc = """
        Ticket Title: Enhance User Profile Management Module

Description:

Objective:
Improve the existing User Profile Management module to provide a more intuitive and personalized experience for our users.

Details:

Technical Enhancements:

User Profile Page:

Implement dynamic rendering of user profiles with HTML, CSS, and JavaScript to enhance the visual presentation.
Integrate responsive design principles for a seamless user experience across devices.
Utilize AJAX for asynchronous data loading to improve page load times.
Skills Display:

Enhance the skills section to dynamically showcase a user's proficiency in coding languages such as Python, JavaScript, and Java.
Implement a tag-based system for easy categorization and display of technical skills.
Integration with External APIs:

Explore and integrate relevant external APIs (e.g., GitHub API) to automatically fetch and display a user's latest coding projects and contributions.
Ensure secure handling of API keys and data privacy.
Soft Skills Integration:

Communication:

Implement a user-friendly interface to allow users to input and showcase their soft skills such as communication, teamwork, and leadership.
Provide a rating system or descriptive input for users to self-assess their soft skills.
User Feedback Mechanism:

Introduce a user feedback mechanism to collect testimonials or endorsements from colleagues, mentors, or project collaborators.
Display aggregated feedback on the user profile in a visually appealing format.
Acceptance Criteria:

User profiles are visually enhanced with HTML, CSS, and JavaScript.
Coding languages and technical skills are dynamically displayed and categorized.
External APIs fetch and display relevant coding projects on the user profile.
Soft skills are incorporated into the user profile, allowing self-assessment and display.
User feedback mechanism is implemented and testimonials are displayed on the user profile.
Code is well-documented, modular, and adheres to coding standards.
Notes:

Collaborate with the UX/UI team for design considerations.
Ensure compatibility with various browsers and devices.
Conduct thorough testing to validate the functionality and performance improvements.

        """
        text = generate_skills(path, "pdf")
        # return an object that has the desc, path, and the similairity ranking
        similairity = cosine_sim(path, desc)
        return jsonify({'status':'success', 'desc': desc, 'path': path,'similairity': similairity})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})



if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=3000)
