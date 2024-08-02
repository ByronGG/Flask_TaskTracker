from flask import request, jsonify, Blueprint
from src.models.task import Task
from src.database import db

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
def add_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=data.get('due_date')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201