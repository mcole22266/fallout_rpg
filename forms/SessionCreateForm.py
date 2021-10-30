from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SessionCreateForm(FlaskForm):
    sessionName = StringField(
        'Session Name',
        validators=[DataRequired()]
        )
    submit = SubmitField('Create Session')
