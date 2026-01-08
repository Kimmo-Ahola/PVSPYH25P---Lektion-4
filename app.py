# install this package:
# flask
#
# Then we install these
# flask-sqlalchemy pymysql flask-migrate
#
# Then we install these
# python-dotenv livereload
import os
from dotenv import load_dotenv
from dataclasses import dataclass
from flask import Flask, render_template
from flask_migrate import Migrate
from database import db
import models
from models.user import User, seedData

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)
migrate = Migrate(app, db)


@dataclass
class UserClass:
    id: int
    name: str
    city: str


@app.route("/users-table-class")
def users_table_class():
    users = [
        UserClass(1, "Kimmo", "Köping"),
        UserClass(2, "Marko", "Köping"),
        UserClass(3, "Minna", "Köping"),
    ]
    return render_template("users-table-class.html", users=users)


@app.route("/users-table")
def users_table():
    users = [
        {"name": "Sara", "age": 17, "city": "Göteborg"},
        {"name": "Lars", "age": 24, "city": "Köping"},
        {"name": "Stefan", "age": 32, "city": "Stockholm"},
        {"name": "Anders", "age": 100, "city": "Västerås"},
    ]
    return render_template("users-table.html", users=users)


@app.route("/users")
def users():
    users = ["Knatte", "fnatte", "tjatte"]
    return render_template("users.html", users=users)


@app.route("/another-route")
def new_route():
    name = "Kimmo"
    age = 34
    return render_template("loop.html", name=name, age=age)


@app.route("/recipe/<int:number>")
def recipe(number: int):
    return render_template(f"recipe-{number}.html")


@app.route("/")
def index():
    users = db.session.query(User).all()
    return render_template("home.html", users=users)


if __name__ == "__main__":
    with app.app_context():
        seedData(db)

    app.run(debug=True)
