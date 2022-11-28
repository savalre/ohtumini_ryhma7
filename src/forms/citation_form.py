"""
Citation form for app.py/routes.py
Currently holds booktype, could possibly hold all types in the future
"""


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, Optional

class BookCitationForm(FlaskForm):
    """
    Form for book type citation
    """

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

    volume = IntegerField('volume', validators=[Optional()],
        render_kw={'placeholder': 'Volume...'})
    series = IntegerField('series', validators=[Optional()],
        render_kw={'placeholder': 'Series...'})
    address = StringField('address', validators=[Optional()],
        render_kw={'placeholder': 'Address...'})
    edition = StringField('edition', validators=[Optional()],
        render_kw={'placeholder': 'Edition...'})
    month = StringField('month', validators=[Optional()],
        render_kw={'placeholder': 'Month...'})
    note = StringField('note', validators=[Optional()],
        render_kw={'placeholder': 'Note...'})
    key = StringField('key', validators=[Optional()],
        render_kw={'placeholder': 'Key...'})
    url = StringField('url', validators=[Optional()],
        render_kw={'placeholder': 'Url...'})
