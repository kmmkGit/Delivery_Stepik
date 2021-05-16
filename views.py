import random

from flask import flash, session, redirect, request, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func

from app import app, db, manager
from models import User, Dish, Category, Order
from forms import OrderForm, RegisterForm, LoginForm


@manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# главная
@app.route('/', methods=["POST", "GET"])
def view_main():
    category = db.session.query(Category).all()
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
            total=db.session.query(func.sum(Dish.price)).filter(Dish.id.in_(session["cart"])).scalar(),
            status="good",
            phone=form.phone.data,
            address=form.address.data,
            user=db.session.query(User).get(current_user.get_id()),
            dish=dish.all()
        )
        db.session.add(order)
        db.session.commit()
        session.pop('cart', None)
        return redirect(url_for('view_ordered'))
    return render_template('cart.html', form=form)


# добавление в корзину
@app.route('/addtocart/<int:dish_id>/')
def view_addtocart(dish_id):
    cart = session.get("cart", [])
    if dish_id not in cart:
        cart.append(dish_id)
        session["cart"] = cart
    flash('Блюдо добавлено в корзину')
    return redirect(url_for('view_cart'))


# удаление из корзины
@app.route('/delfromcart/<int:dish_id>/')
def view_delfromcart(dish_id):
    if dish_id in session["cart"]:
        session["cart"].remove(dish_id)
        flash('Блюдо удалено из корзины')
    else:
        flash('Такого блюда нет в корзине')
    return redirect(url_for('view_cart'))


# личный кабинет
@app.route('/account/', methods=["POST", "GET"])
@login_required
def view_account():
    orders = db.session.query(Order).filter(Order.user_id == current_user.get_id())
    return render_template('account.html', orders=orders)


# регистрация
@app.route('/register/', methods=["POST", "GET"])
def view_register():
    form = RegisterForm()
#    print('Register method ', request.method)
#    print(form.email.data, form.password.data)
#    print(form.validate_on_submit())
    if request.method == "POST" and form.validate_on_submit():
        if db.session.query(User).filter(User.email == form.email.data).scalar():
            form.email.errors.append("Такой пользователь уже зарегистрирован")
            return render_template("register.html", form=form)
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        print('Register Yes')
        return redirect(url_for("view_login"))
    return render_template('register.html', form=form)


@app.route('/login/', methods=["POST", "GET"])
def view_login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = db.session.query(User).filter(User.email == form.email.data).scalar()
        if user:
            login_user(user)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("view_main"))
        else:
            form.email.errors.append("Неверно введено имя или пароль")
    return render_template("login.html", form=form)


# выход
@app.route('/logout/', methods=["POST", "GET"])
def view_logout():
    logout_user()
    return redirect(url_for("view_main"))


"""
@app.after_request
def after_request(response):
    if response.status_code == 401:
        return redirect(url_for("view_login") + "?next=" + request.url) 
"""


# подтверждение отправки
@app.route('/ordered/')
def view_ordered():
    return render_template('ordered.html')


@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена", error


@app.errorhandler(500)
def page_not_found(error):
    return "Ошибка сервера", error


@app.context_processor
def total_cart():
    dishes = db.session.query(Dish).filter(Dish.id.in_(session.get("cart", []))).all()
    total = db.session.query(func.sum(Dish.price)).filter(Dish.id.in_(session.get("cart", []))).scalar()
    if not total:
        total = 0
    return dict(dishes=dishes, total=total)


@app.template_filter('shuffle')
def filter_shuffle(seq, num_first, num_end):
    result = list(seq)
    random.shuffle(result)
    return result[num_first:num_end]


@app.template_filter('formatdatetime')
def filter_datetime(value, format_date="%d %b"):
    return "" if value is None else value.strftime(format_date)

