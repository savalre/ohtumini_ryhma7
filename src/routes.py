from flask import render_template
from app import app
#Will be needed in future
#from flask import redirect, session, request, url_for
from forms.citation_form import BookCitationForm
from repositories.citation_repository import CitationRepository

@app.route("/")
def index():
    """
    Main page
    No parameters
    Returns: html for front page (for use by flask)
    """
    return '<h1>Flask</h1>'

@app.route("/book", methods=['GET', 'POST'])
def book():
    form = BookCitationForm()
    if form.validate_on_submit():
        # Form values to be passed to Citation Class in the future, accessible by: form.<field>.data
        return ('<h1>' + form.cite.data + form.author.data +
                form.title.data + str(form.year.data) + form.publisher.data + '</h1>')

    return render_template('/book.html', form = form)

@app.route("/citations")
def list_citations():
    list = CitationRepository.list_citations()
    return render_template("citations.html", citation_list = list)
