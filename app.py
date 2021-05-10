from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db, User, Dish, Category, Order
# from forms import LoginForm, RegistrationForm, ChangePasswordForm


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# from views import *


if __name__ == '__main__':
    app.run(debug=True)
