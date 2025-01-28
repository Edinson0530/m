from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class VideoForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    description = TextAreaField("Descripción")
    video_file = FileField("Video", validators=[DataRequired()])
    submit = SubmitField("Subir")