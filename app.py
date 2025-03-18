"""Libery imports"""
from flask import Flask, request, jsonify
""" past imports """
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

# Method POST (Inclui uma nova task)
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control ,title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

# Method GET (Visualiza todas tasks)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

# Method GET (Visualiza somente uma task)
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

# Methdd PUT (Atualiza uma task)
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t 
            break
    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarfea deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)

""" 
	"title": "Estudar python",
	"description": "Flask api"

    "title": "Ir para a academia",
	"description": "treinar ombro"
"""