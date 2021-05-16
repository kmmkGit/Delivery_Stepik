from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from config import Config
from models import db
from admin import admin


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
manager = LoginManager(app)
admin.init_app(app)


from views import *

if __name__ == '__main__':
    app.run(debug=True)
