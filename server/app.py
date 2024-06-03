import os
from dotenv import load_dotenv
from uuid import uuid4

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import json

from db import cnx, cursor as DB

load_dotenv()
app = Flask(__name__)
CORS(app)


def get_request_data() -> dict:
    return json.loads(request.data.decode())['data']


def generate_response(msg: str, code: int):
    r = make_response(msg)
    r.status_code = code
    return r


@app.post('/signup')
def signup():
    user = get_request_data()

    DB.execute(
        f"SELECT * FROM users WHERE username=%s or email=%s", (user['name'], user['email']))

    if list(DB) != []:
        return generate_response('User Already Exising', 300)

    DB.execute(
        "INSERT INTO users VALUES(%s, %s, %s, %s)", (str(uuid4()).replace('-', ''), user['name'], user['email'], user['pwd']))
    cnx.commit()

    return generate_response('User Inserted', 201)


@app.post('/login')
def login():
    user = get_request_data()

    DB.execute(
        f"SELECT * FROM users WHERE (username=%s or email=%s) and password=%s", (user['name'], user['name'], user['pwd']))

    row = DB.fetchone()
    if row:
        user = {
            'id': row[0], 'name': row[1], 'email': row[2]
        }
        return generate_response(jsonify(user), 200)

    return generate_response('User Not Found', 301)


@app.get('/list/<id>')
def get_list(id: str):
    DB.execute(f"SELECT * FROM books WHERE userID=%s", (id,))
    result = list(DB)
    books_info: list[dict] = []

    for row in result:
        books_info.append({
            'id': row[0],
            'status': row[1]
        })

    if not result:
        return generate_response('User Not Found', 404)
    return generate_response(jsonify(books_info), 200)


@app.get('/book/<book_id>/<user_id>')
def get_book_status(book_id: str, user_id: str):

    DB.execute(f"SELECT * FROM books WHERE ID=%s AND userID=%s",
               (book_id, user_id))
    result = list(DB)

    if not result:
        return generate_response('Book Not Found', 404)
    data = {'bookID': result[0][0],
            'bookStatus': result[0][1], 'user': result[0][1]}
    return generate_response(jsonify(data), 200)


@app.post('/remove_book')
def remove_book():
    data = get_request_data()

    DB.execute(
        f"DELETE FROM books WHERE ID=%s AND userID=%s", (data['bookID'], data['userID']))
    cnx.commit()

    if DB.rowcount == 0:
        return make_response('No Correspondition Found', 404)
    return make_response('Row Dropped', 200)


@app.post('/insert_book')
def insert_book():
    data = get_request_data()
    DB.execute('''INSERT INTO books(ID, status, userID)
               VALUES(%s, %s, %s)
               ON DUPLICATE KEY UPDATE status=VALUES(status)
               ''', (data['bookID'], data['status'], data['userID']))
    cnx.commit()
    if DB.rowcount == 0:
        return make_response('Not Found', 404)
    return make_response('Done', 200)


app.run(debug=True, port=os.getenv('SERVER_PORT'))
cnx.close()
