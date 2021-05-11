import os

current_path = os.path.dirname(os.path.realpath(__file__))

# db_path = "sqlite:///" + current_path + "\\test.db"


class Config:
    DEBUG = True
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_delivery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# "postgresql+psycopg2://postgres:Maxim@127.0.0.1:5432/postgresdb"
# os.environ.get("DATABASE_URL")
# 'sqlite:///my_delivery.db'
# app.config['SQLALCHEMY_ECHO'] = True
