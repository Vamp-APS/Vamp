# app.py

from flask import Flask

from database.database import Database

# Create a Flask application
app = Flask(__name__)


# Define a route and view function
@app.route("/")
def index():
    return "Hello, World!"


# Run the Flask application
if __name__ == "__main__":
    Database("mysql://root:password@localhost:3306/mysql")
    app.run(debug=True)
