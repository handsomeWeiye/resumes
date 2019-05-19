from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask
from flask_wtf import CSRFProtect
from myresume.settings import config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(config['production'])
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
moment = Moment(app)


from myresume import views




