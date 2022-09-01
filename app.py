from crypt import methods
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0
db = SQLAlchemy(app)

# Models
class Todo(db.Model):
    __tablename__="todo"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)



@app.route("/edit")
def home():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@app.route("/")
def list():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)