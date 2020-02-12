from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm):
    answer = StringField('answer', validators=[DataRequired()])
    submit = SubmitField('submit')
