from app import app
from flask import render_template
#Will be needed in future
#from flask import redirect, session, request, url_for

from forms.add_citation_form import CitationForm

@app.route("/", methods=['GET', 'POST'])
def add():
    """
    Main page
    No parameters
    Returns: html for front page (for use by flask)
    """

    form = CitationForm()
    if form.validate_on_submit():
        # Form values to be passed to Citation Class in the future, accessible by: form.<field>.data
        return '<h1>' + form.cite.data + form.author.data + form.title.data + str(form.year.data) + '</h1>'
    return render_template('/add.html', form = form)
