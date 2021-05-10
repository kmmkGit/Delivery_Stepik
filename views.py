from functools import wraps

from flask import abort, flash, session, redirect, request, render_template

from app import app, db
from models import User, Dish, Category, Order
from forms import LoginForm, RegistrationForm, ChangePasswordForm


@app.route('/')
# главная
def view_main():
    return render_template('main.html')


@app.route('/cart/', methods=["POST", "GET"])
# корзина
def view_cart():
    form = SortTeachers()
    teachers_query = db.session.query(Teacher)
    teachers_sort = []
    if request.method == 'POST':
        sort_type = form.sort_type.data
        if sort_type == form.sort_type.choices[0][0]:
            teachers_sort = teachers_query.order_by(func.random()).all()
        if sort_type == form.sort_type.choices[1][0]:
            teachers_sort = teachers_query.order_by(Teacher.rating.desc()).all()
        if sort_type == form.sort_type.choices[2][0]:
            teachers_sort = teachers_query.order_by(Teacher.price.desc()).all()
        if sort_type == form.sort_type.choices[3][0]:
            teachers_sort = teachers_query.order_by(Teacher.price).all()
    else:
        teachers_sort = teachers_query.all()
    return render_template('cart.html', form=form)


@app.route('/account/', methods=["POST", "GET"])
# личный кабинет
def view_account():

    return render_template('account.html')


@app.route('/auth/', methods=["POST", "GET"])
# аутентификация
def view_auth():

    return render_template('auth.html')


@app.route('/register/', methods=["POST", "GET"])
# регистрация
def view_register():

    return render_template('register.html')


@app.route('/logout/', methods=["POST", "GET"])
# регистрация
def view_logout():

    return render_template('logout.html')


@app.route('/ordered/', methods=["POST", "GET"])
# регистрация
def view_ordered():

    return render_template('ordered.html')


@app.route('/addtocart/', methods=["POST", "GET"])
# регистрация
def view_addtocart():

    return render_template('addtocart.html')
