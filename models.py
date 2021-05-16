from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
import pytz


db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), server_default="false", nullable=False)
    orders = db.relationship("Order", back_populates="user")


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    csv_id = db.Column(db.Integer)
    dishes = db.relationship("Dish", back_populates="category")


dish_order_association = db.Table(
    'dishes_orders',
    db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
)


class Dish(db.Model):
    __tablename__ = "dishes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float())
    description = db.Column(db.String())
    picture = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship(
        "Category", back_populates="dishes"
    )
    order = db.relationship(
        "Order", secondary=dish_order_association, back_populates="dish"
    )


def current_time():
    return datetime.now(pytz.timezone('Europa/Moscow'))


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=current_time)
    total = db.Column(db.Float())
    status = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(
        "User", back_populates="orders"
    )
    dish = db.relationship(
        "Dish", secondary=dish_order_association, back_populates="order"
    )
