import re

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import RadioField
from wtforms import SubmitField
from wtforms import HiddenField
from wtforms import SelectField
from wtforms.validators import InputRequired, Length


class OrderForm(FlaskForm):
    name = StringField("Вас зовут", [InputRequired(message="Необходимо указать имя"),
                                     Length(min=2, max=50, message="Имя %(min)d - %(max)d символов")])
    phone = StringField("Ваш телефон", [InputRequired(message="Необходимо ввести ваш номер телефона"),
                                        Length(max=15, message="Слишком много символов в номере телефона")])
    submit = SubmitField('Записаться на пробный урок')
    weekday = HiddenField("День недели для записи")
    time = HiddenField("Часы занятий для записи")
    teacher = HiddenField("Id учителя")



