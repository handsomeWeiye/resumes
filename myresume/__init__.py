from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from myresume.settings import config

app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)



