import os
from flask import jsonify
from Models.models import db, Todo


class TodoController(object):
    def __init__(self):
        pass

    @staticmethod
    def create(request):
        try:
            if not request.json['name']:
                data = {
                    "success": False,
                    "payload": {
                        "message": "Empty Todo Name"
                    }
                }
                return jsonify({"TodoData": data})

            if request.json['name']:
                # Create a new To-do
                new_todo = Todo(name=request.json['name'], description=request.json['description'])
                # Add the new user to the session
                db.session.add(new_todo)
                # Commit the transaction to save the user to the database
                db.session.commit()
                data = {
                    "success": True,
                    "payload": {
                        "message": {
                            'id': new_todo.id,
                            'name': new_todo.name,
                            'description': new_todo.description
                        }
                    }
                }
                return jsonify({"TodoData": data})
        except Exception as exc:
            return jsonify({"Create Error": str(exc)})

    @staticmethod
    def search_read():
        try:
            todos = Todo.query.all()
            todos_list = [{'id': todo.id, 'name': todo.name, 'description': todo.description} for todo in todos]

            if not len(todos_list):
                data = {
                    "success": False,
                    "payload": {
                        "message": "Empty Todo"
                    }
                }
                return jsonify({"TodoData": data})

            else:
                data = {
                    "success": True,
                    "payload": todos_list
                }
                return jsonify({"TodoData": data})
        except Exception as exc:
            return jsonify({"Get todos Error": str(exc)})

    @staticmethod
    def todo_get(id):
        try:
            todo = Todo.query.get(id)
            if not todo:
                data = {
                    "success": False,
                    "payload": {
                        "message": "Todo not found"
                    }
                }
                return jsonify({"TodoData": data})

            data = {
                "success": True,
                "payload": {
                    'id': todo.id,
                    'name': todo.name,
                    'description': todo.description
                }
            }
            return jsonify({"TodoData": data})
        except Exception as exc:
            return jsonify({"Get a todo Error": str(exc)})