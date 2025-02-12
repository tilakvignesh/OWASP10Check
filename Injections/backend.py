from flask import Flask, request, redirect, url_for, Response
import sqlite3
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

"""
    username = "'Alice' OR 1=1; --"
    password = 'password'
"""

@app.route('/login', methods=['POST'])
def login():
    try:
        connection = sqlite3.connect('injections.db')
        data = request.get_json()
        username = data['username']
        password = data['password']
        cursor = connection.cursor()
        command = 'SELECT * FROM user WHERE username= ' + f'"{username}"' + ' AND password= ' + f'"{password}"'
        cursor.execute(command)
        user = cursor.fetchall()
        resp = json.dumps(user)
        return Response(resp, status=200)
    except Exception as e:
        print(e)
        return Response({
            'msg': 'Invalid credentials'
        }, status=401)

if __name__ == "__main__":
    app.run(debug=True)
