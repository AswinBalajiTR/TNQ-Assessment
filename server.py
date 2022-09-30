from flask import Flask, request
from mysql.connector import connect, Error

# INIT
app = Flask(__name__)
db = connect(
    host="localhost",
    user="testadmin",
    password="password",
    database="test"
)
print("Connected to MySQL database")

# DB RELATED

# TABLE CREATIONS ARE ASSUMED TO BE DONE ALREADY
# NOT USING ANY ORM TO KEEP IT SIMPLE

# TABLES IN DATABASE:
#   test: id, a, b, sum, division, multiplication, subtraction

# ROUTES
@app.route('/', methods=['POST'])
def index():
    body = request.get_json()
    a, b = body.get("a", None), body.get("b", None)

    if a is not None and b is not None:
        cursor = db.cursor()
        output = {}

        output["sum"] = a + b
        output["division"] = a / b
        output["multiplication"] = a * b
        output["subtraction"] = a - b

        # db operations
        try:
            cursor.execute(
                "INSERT INTO test (a, b, sum, division, multiplication, subtraction) VALUES (%s, %s, %s, %s, %s, %s)", 
                (a, b, output["sum"], output["division"], output["multiplication"], output["subtraction"])
            )
            db.commit()
        except Error as err:
            print("ERROR: ", err)
            cursor.close()
            return {"status": "error", "message": "Something went wrong"}, 400

        cursor.close()
        return {"status": "ok", "result": output}, 200

    return {"status": "error", "message": "Missing a or b"}, 400