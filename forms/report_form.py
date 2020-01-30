# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    name = StringField('Введите ваш отчёт об ошибке: ', validators=[DataRequired()])
