import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {'id': 1, 'name': 'Erick'},
    {'id': 2, 'name': 'Tim'},
    {'id': 3, 'name': 'Steve'}
]


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


if __name__ == '__main__':
    app.run(port=5000)
