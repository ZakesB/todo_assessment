'''
To-Do API
'''

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from Connections.config import app
from Models.models import db, Todo
from Controllers.controllers import TodoController

auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/api/v1/todo/about/us', methods=['GET'])
@cross_origin()
@auth.error_handler
def abouttodo():
    return jsonify({'todo': 'Welcome to To-Do! Where todos made easy.'})


@app.route('/api/v1/todos', methods=['GET'])
@cross_origin()
@auth.error_handler
def get_list_todos():
    res = TodoController.search_read()
    return make_response(res, 200)


@app.route('/api/v1/todo/<int:id>', methods=['GET'])
@cross_origin()
@auth.error_handler
def get_todo(id):
    res = TodoController.todo_get(id)
    return make_response(res, 200)


@app.route('/api/v1/todo', methods=['POST'])
@cross_origin()
def create_todo():
    try:
        if not request.json or not 'name' in request.json:
            abort(400)
        res = TodoController.create(request)

        return make_response(res, 200)
    except Exception as exc:
        return make_response(jsonify({"[ERROR] creating todo func": str(exc)}))


if __name__ == '__main__':
    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(port=5001)