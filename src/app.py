from flask import Flask, jsonify, request, json 
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return jsonify(todos)
    ##print("Incoming request with the following body", request_body)
    ##return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

todos = [
  { "label": "My first task", "done": True },
  { "label": "My second task", "done": False } ]


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)