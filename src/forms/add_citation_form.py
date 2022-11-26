from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, Optional

class CitationForm(FlaskForm):
    cite = StringField('cite', validators=[InputRequired(), Length(min=4)], render_kw={'placeholder': 'Cite...'})
    author = StringField('author', validators=[InputRequired(), Length(min=4)], render_kw={'placeholder': 'Author...'})
    title = StringField('title', validators=[InputRequired(), Length(min=4)], render_kw={'placeholder': 'Title...'})
    year = IntegerField('year', validators=[InputRequired()], render_kw={'placeholder': 'Year...'})

    booktitle = StringField('booktitle', validators=[Optional(), Length(min=4)], render_kw={'placeholder': 'Book title...'}, default="")
    journal = StringField('journal', validators=[Optional(), Length(min=4)], render_kw={'placeholder': 'Journal...'})
    volume = IntegerField('volume', validators=[Optional()], render_kw={'placeholder': 'Volume...'})
    pages = StringField('pages', validators=[Optional(), Length(min=4)], render_kw={'placeholder': 'Pages...'})
    publisher = StringField('publisher', validators=[Optional(), Length(min=4)], render_kw={'placeholder': 'Publisher...'})

    