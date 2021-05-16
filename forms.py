from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import HiddenField
from wtforms.validators import InputRequired, DataRequired, Length, Email
import email_validator


class OrderForm(FlaskForm):
    name = StringField("Имя", [InputRequired(message="Необходимо указать имя")])
    address = StringField("Адрес", [InputRequired(message="Необходимо ввести ваш адрес")])
    phone = StringField("Ваш телефон", [InputRequired(message="Необходимо ввести ваш номер телефона")])
    submit = SubmitField('Оформить заказ')


class RegisterForm(FlaskForm):
    email = StringField("Электропочта", [
        Email(message="Необходимо указать почту"),
        InputRequired(message="Необходимо указать почту"),
    ])
    password = PasswordField("Пароль", [
        InputRequired(message="Необходимо ввести ваш пароль"),
        Length(min=5, message="Слишком мало символов в пароле, минимум 5")
    ])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField("Электропочта", [
        Email(message="Необходимо указать почту"),
        InputRequired(message="Необходимо указать почту"),
    ])
    password = PasswordField("Пароль", [
        InputRequired(message="Необходимо ввести ваш пароль"),
        Length(min=5, message="Слишком мало символов в пароле, минимум 5")
    ])
    submit = SubmitField('Войти')
