from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "How to write a secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xkigwepwonngnm:ecb49091a14199bee125a56621e06569b7383c6b6bc49c3026cfb8969e7b1d72@ec2-23-23-241-119.compute-1.amazonaws.com:5432/d6h0fkbjbo6dnn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

UPLOAD_FOLDER = "./app/static/uploads"

app.config.from_object(__name__)
from app import views, models
