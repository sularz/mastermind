from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AnswerForm(FlaskForm):
    answer = StringField('answer', validators=[DataRequired(), Length(min=8, max=8)])
    submit = SubmitField('submit')
