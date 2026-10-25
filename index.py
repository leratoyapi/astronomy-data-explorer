# here will the apis
# alwasy put the import at the top of the file don forget.

from flask import Flask, jsonify
from conn import conn


app = Flask(__name__)

@app.route("/")
def light_positive():
    return "<p>I am building something as part of my learning challenge</p>"



# here is the syntax :
# requests.get(url, params={key: value}, args)

# args means zero or more of the named arguments in the parameter table below.

# Example:
# define your url =...
# requests.get(url, timeout=2.50)

# creating a route that will call the apod data
@app.route("/apod")
def get_all_apods():
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM apod")
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__=="__main__":
    app.run(debug=True)