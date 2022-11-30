"""
Routes module for flask app
Used by app.py
"""
from flask import render_template, redirect
from app import app
from entities.citation import Citation
#Will be needed in future
#from flask import redirect, session, request, url_for
from forms.citation_form import BookCitationForm
from repositories.citation_repository import CitationRepository as cite_repo

@app.route("/")
def index():
    """
    Home page
    """
    return render_template("index.html")

#Disable error, because the code is fine for now, and is going to be replaced in this sprint
@app.route("/book", methods=['GET', 'POST'])
def book(): # pylint: disable=too-many-branches
    """
    Add book type citation page
    Uses BookCitationForm from forms
    Returns: html for book type citation page & values from form.validate_on_submit

    """
    form = BookCitationForm()
    if form.validate_on_submit():
        # Form values to be passed to Citation Class in the future, accessible by: form.<field>.data
        fields = []
        author = form.author.data
        title = form.title.data
        year = form.year.data
        publisher = form.publisher.data
        volume = form.volume.data
        series = form.series.data
        address = form.address.data
        edition = form.edition.data
        month = form.month.data
        note = form.note.data
        key = form.key.data
        url = form.url.data

        if author:
            fields.append(("author", author))
        if title:
            fields.append(("title", title))
        if year:
            fields.append(("year", str(year)))
        if publisher:
            fields.append(("publisher", publisher))
        if volume:
            fields.append(("volume", str(volume)))
        if series:
            fields.append(("series", str(series)))
        if address:
            fields.append(("address", address))
        if edition:
            fields.append(("edition", edition))
        if month:
            fields.append(("month", month))
        if note:
            fields.append(("note", note))
        if key:
            fields.append(("key", key))
        if url:
            fields.append(("url", url))

        citation = Citation("RANDOM_CITE_AS_TAG", form.cite.data, fields)
        cite_repo().store_citation(0, citation)
        return redirect("/book")
    #list = CitationRepository().list_citations(0)
    #for c in list:
        #print(c.entryname + "(" + c.cite_as + "), field_types: ")
        #for f in c.fieldtypes:
            #print(f)
    return render_template('/book.html', form = form)

@app.route("/citations")
def list_of_citations():
    """
    A page for diplaying all the citations of a user
    """
    # CHANGE DEFAULT VALUE OF USER_ID TO LOGGED IN USER ONCE SESSIONS HAVE BEEN ADDED!
    return render_template("citations.html", citation_list = cite_repo().list_citations(0))
