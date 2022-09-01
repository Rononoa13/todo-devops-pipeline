from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# 
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/base")
def home1():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)