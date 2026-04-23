

from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
import database

app= Flask(__name__)

database.init_database() # create table on startup


@app.route("/")
def home():
    return jsonify({"message": "Server Online"}) , 200

# URL parameter — receives an integer id
@app.route("/persons")
def get_persons():
    conn  = database.get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(""" select * from persons """)
    row = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(list(row)) , 201

@app.route("/persons", methods=["POST"])
def create_person():
    json_data = request.get_json()
    conn  = database.get_connection()
    cur = conn.cursor()
    cur.execute(""" insert into persons 
                    (first_name, last_name, address, age)
                    values 
                    (%s, %s, %s, %s)
                 """, 
                 ( json_data["first_name"], json_data["last_name"], json_data["address"], json_data["age"] ) )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Person created"})


if __name__ == "__main__":
    app.run(debug=True)