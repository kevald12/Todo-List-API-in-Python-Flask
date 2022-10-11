from flask import Flask,jsonify
app = Flask(__name__)
from flask import request



todos = [ 
    { "label": "My first task", "done": False }, 
    { "label": "My Second task", "done": False } 
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_text = jsonify(todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos [position]
    json_text = jsonify(todos)
    return jsonify(todos)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)