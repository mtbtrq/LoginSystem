import sqlite3
import flask
from flask import request, redirect

app = flask.Flask(__name__)

databaseName = "database.db"
tableName = "login_details"
mainDatabase = sqlite3.connect(databaseName)
crsr = mainDatabase.cursor()

try:
    crsr.execute(f"""
    CREATE TABLE IF NOT EXISTS {tableName} (
        email text,
        password text,
        username text
    )
    """)
except sqlite3.OperationalError:
    print("Table Already Exists! Skipping the creation of table...")

mainDatabase.commit()
mainDatabase.close()

@app.route("/", methods=["GET"])
def mainPage():
    return """
    <h1>Welcome!</h1>
    <p><code>/get</code> to view all records</p>
    <p><code>/post</code> to insert a new record</p>
    """

@app.route('/get', methods=['GET'])
def get():
    try:
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {tableName}")
        dbData = cursor.fetchall()
        connection.close()

        returnData = {
            "success": True,
            "data": dbData
        }

        return returnData

    except Exception as e:
        return {
            "success": False,
            "cause": e
        }

@app.route("/post", methods=["POST", "GET"])
def post():
    try:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO {tableName} values (?, ?, ?)", (email, password, username))
        connection.commit()
        connection.close()

        return "Signed In!"
    except Exception as e:
        return {
            "success": False,
            "cause": e
        }

app.run()