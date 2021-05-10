import re

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import RadioField
from wtforms import SubmitField
from wtforms import HiddenField
from wtforms import SelectField
from wtforms.validators import InputRequired, Length


class FormRequest(FlaskForm):
    name = StringField("Вас зовут", [InputRequired(message="Необходимо указать имя"),
                                     Length(min=2, max=50, message="Имя %(min)d - %(max)d символов")])
    phone = StringField("Ваш телефон", [InputRequired(message="Необходимо ввести ваш номер телефона"),
                                        Length(max=15, message="Слишком много символов в номере телефона")])
    goal = RadioField('Какая цель занятий?', choices=request_goal_choices, default=request_goal_choices[0][0])
    time = RadioField('Сколько времени есть?', choices=time_have, default=time_have[0][0])
    submit = SubmitField('Найдите мне преподавателя')


class BookingToTeacher(FlaskForm):
    name = StringField("Вас зовут", [InputRequired(message="Необходимо указать имя"),
                                     Length(min=2, max=50, message="Имя %(min)d - %(max)d символов")])
    phone = StringField("Ваш телефон", [InputRequired(message="Необходимо ввести ваш номер телефона"),
                                        Length(max=15, message="Слишком много символов в номере телефона")])
    submit = SubmitField('Записаться на пробный урок')
    weekday = HiddenField("День недели для записи")
    time = HiddenField("Часы занятий для записи")
    teacher = HiddenField("Id учителя")


class SortTeachers(FlaskForm):
    sort_type = SelectField("Сортировка преподавателей",
                            choices=[("Случайно", "В случайном порядке"),
                                     ("Рейтинг", "Сначала лучшие по рейтингу"),
                                     ("Дорогие", "Сначала дорогие"),
                                     ("Недорогие", "Сначала недорогие")])
    submit = SubmitField('Сортировать')

