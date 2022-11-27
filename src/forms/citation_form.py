from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, Optional

class BookCitationForm(FlaskForm):
    cite = StringField('cite', validators=[InputRequired(), Length(min=4)],
        render_kw={'placeholder': 'Cite...'})
    author = StringField('author', validators=[InputRequired(), Length(min=4)],
        render_kw={'placeholder': 'Author...'})
    title = StringField('title', validators=[InputRequired(), Length(min=4)],
        render_kw={'placeholder': 'Title...'})
    year = IntegerField('year', validators=[InputRequired()],
        render_kw={'placeholder': 'Year...'})
    publisher = StringField('publisher', validators=[InputRequired(), Length(min=4)],
        render_kw={'placeholder': 'Publisher...'})
