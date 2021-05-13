from functools import wraps
import random

from flask import abort, flash, session, redirect, request, render_template, url_for
from sqlalchemy.sql.functions import current_user
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, manager
from models import User, Dish, Category, Order
from forms import OrderForm, RegisterForm, LoginForm


@manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# главная
@app.route('/')
def view_main():
    category = db.session.query(Category).all()

#    dishes = [dish for dish in category.dishes]
    return render_template('main.html', category=category)


# корзина
@app.route('/cart/', methods=["POST", "GET"])
def view_cart():
    form = OrderForm()
    dish = db.session.query(Dish).filter(Dish.id.in_(session["cart"]))
    if request.method == "POST" and form.validate_on_submit() and current_user.is_authenticated:
        if not dish:
            flash('Вы ничего не выбрали')
            return render_template('cart.html', form=form)
        order = Order(
            total=sum(dish_item.price for dish_item in dish),
            status="good",
            phone=form.phone.data,
            address=form.address.data,
            user=db.session.query(User).get(current_user.get_id()),
            dish=dish.all()
        )
        db.session.add(order)
        db.session.commit()
        session.pop('cart', None)
        return redirect(url_for('ordered_view'))
    return render_template('cart.html', form=form)


# личный кабинет
@app.route('/account/', methods=["POST", "GET"])
@login_required
def view_account():
    orders = db.session.query(Order).filter(Order.user_id == current_user.get_id())
    return render_template('account.html', orders=orders)


# аутентификация
@app.route('/auth/', methods=["POST", "GET"])
def view_auth():

    return render_template('auth.html')


# регистрация
@app.route('/register/', methods=["POST", "GET"])
def view_register():

    return render_template('register.html')


# выход
@app.route('/logout/', methods=["POST", "GET"])
def view_logout():

    return render_template('logout.html')


# подтверждение отправки
@app.route('/ordered/', methods=["POST", "GET"])
def view_ordered():

    return render_template('ordered.html')


# добавление в корзину
@app.route('/addtocart/<int:dish_id>/')
def view_addtocart(dish_id):
    dish = db.session.query(Dish).get_or_404(dish_id)
    cart = session.get("cart", [])
    if dish_id not in cart:
        cart.append(dish_id)
        session["cart"] = cart
    flash('Товар добавлен в корзину')
    return redirect(url_for('view_cart'))


# удаление из корзины
@app.route('/delfromcart/<int:dish_id>/')
def view_delfromcart(dish_id):
    if dish_id in session["cart"]:
        session["cart"].remove(dish_id)
        flash('Товар удалён из корзины')
    else:
        flash('Такого товара нет в корзине')
    return redirect(url_for('view_cart'))
