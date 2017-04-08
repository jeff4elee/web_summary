from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
login_manager = LoginManager()

if __name__ == 'main':
	app.run(debug=True)

from home import views