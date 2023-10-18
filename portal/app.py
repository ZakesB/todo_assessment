from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

BASE_URL = 'http://localhost:5001'
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create_todo():
    api_url = f"{BASE_URL}/api/v1/todo"
    payload = {
        'name': request.form.get('todo-name'),
        'description': request.form.get('todo-description'),
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(api_url, json=payload, headers=headers)
    print(response)
    if response.status_code == 200:
        # Process the data from the API response
        data = response.json()
        print(data)
        return redirect(url_for('index'))
        #return render_template('success.html', success=True)
    else:
        return "Error: Unable to fetch data from the API"


@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    api_url = f"{BASE_URL}/api/v1/todos"
    response = requests.get(api_url)
    print(response)
    if response.status_code == 200:
        # Process the data from the API response
        data = response.json()
        todos = data['TodoData']['payload']
        print(todos)
        return render_template('todos.html', todos=todos)
    else:
        return "Error: Unable to fetch data from the API"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5002)
