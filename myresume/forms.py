from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    author = StringField('Your name',validators=[DataRequired()])
    body = TextAreaField('Your comment',validators=[DataRequired()])
    submit = SubmitField('Submit')