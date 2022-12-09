from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="Post name",
        name="post-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    body = TextAreaField(validators=[DataRequired()])