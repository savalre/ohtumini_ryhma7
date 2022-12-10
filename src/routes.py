"""
Routes module for flask app
Used by app.py
"""
import json
from flask import render_template, redirect, request, make_response
from app import app
from entities.citation import Citation
from repositories.citation_repository import CitationRepository as cite_repo
from bibtex_generator.bibtex_generator import generate_bibtex_string
from services.citation_service import CitationService as cite_service


@app.route("/")
def index():
    """
    Home page
    """
    return render_template("index.html")

@app.route("/citations")
def list_of_citations():
    """
    A page for diplaying all the citations of a user
    """
    # CHANGE DEFAULT VALUE OF USER_ID TO LOGGED IN USER ONCE SESSIONS HAVE BEEN ADDED!
    return render_template("citations.html", citation_list = cite_repo().list_citations(0))

@app.route("/citations.bib")
def show_bib_file():
    """
    A page for displaying citations in a form
    that can be saved as a .bib file
    """
    citations = cite_repo().list_citations(0)
    if len(citations) == 0:
        return redirect("/citations")
    bibtex = generate_bibtex_string(citations)
    response = make_response(bibtex)
    response.mimetype = "text/plain"
    return response

@app.route("/new", methods=["POST", "GET"])
def new():
    """
    A page for selecting an entry type
    """
    if request.method == "GET":
        return render_template("newcitation.html")
    entry_type = request.form.get("entry_type")
    return new_type(entry_type)


@app.route("/new/<entry_type>")
def new_type(entry_type):
    """
    A page for selecting the field types of the selected entry type.
    The available entry types and their possible field types can be found in data.json.
    """
    with open("data.json", encoding = 'utf-8') as file:
        data = json.load(file)
    if not entry_type in data:
        return redirect("/new")
    list_t = tuple(data[entry_type].items())
    return render_template("entrytypecitation.html", entry_type = entry_type, list = list_t)

@app.route("/new/citation", methods=["POST", "GET"])
def new_citation():
    """
    Functionality for adding a new citation after receving the values from the correct form.
    If the citation is valid, it is stored in the database.
    """
    if request.method == "GET":
        return redirect("/new")

    fields = []
    entry_type = request.form.get("entry_type")
    cite_as = request.form.get("cite_as")

    for field_name in request.form:
        value = request.form.get(field_name)
        if value and field_name != 'cite_as' and field_name != 'entry_type':
            fields.append((field_name, value))

    citation = Citation(cite_as, entry_type, fields)
    cite_serve = cite_service()

    if cite_serve.validate(citation):
        cite_repo().store_citation(0, citation)

    return redirect("/new")
