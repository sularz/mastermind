from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AnswerForm(FlaskForm):
    answer_form = StringField('Tutaj wpisz kod, hakerze!')
    submit = SubmitField('Sprawdz!')
