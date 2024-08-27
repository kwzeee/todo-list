from flask import Flask, g, request
from flask_cors import CORS
import json
import sqlite3


DATABASE = 'todolist.db'
app = Flask(__name__)
CORS(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(e):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/list", methods=['GET', 'POST', 'DELETE'])
def list_api():
    if request.method == 'GET':
        cursor = get_db().cursor()
        cursor.execute('SELECT * FROM Todo')
        items = cursor.fetchall()

        cursor.execute('SELECT * FROM Todo')
        print(cursor.fetchall())
        
        return json.dumps([ (i[0], i[1]) for i in items ])
        

    elif request.method == 'POST':
        data = request.get_json()
        cursor = get_db().cursor()
        print(data['text'])
        cursor.execute('INSERT INTO Todo VALUES (NULL, ?)', (data['text'], ))
        get_db().commit()
        return json.dumps({'succ': 1})
        
    elif request.method == 'DELETE':
        data = request.get_json()
        print(data['id'])
        
        cursor = get_db().cursor()
        cursor.execute('DELETE FROM Todo WHERE id=?', (data['id'], ))
        get_db().commit()
        return json.dumps({'succ': 1})
