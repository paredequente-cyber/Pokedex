from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('hello.html')


if __name__ in "__main__":
  app.run(debug=True)
