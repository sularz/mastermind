from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm):
    answer = StringField('Tutaj wpisz swój kod, hakerze! Wpisuj dozwolone kolory: niebieski, zielony, czarny, czerwony!', validators=[DataRequired()])
    submit = SubmitField('wyślij')
