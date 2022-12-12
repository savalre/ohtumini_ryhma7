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

# pylint: disable=line-too-long, broad-except

@app.route("/")
def index():
    """
    Home page
    """
    return render_template("index.html")

@app.route("/citations")
def list_of_citations():
    """
    A page for diplaying all the citations
    """
    return render_template("citations.html", citation_list = cite_repo().list_citations())

@app.route("/delete", methods=["POST","GET"])
def delete_selected_citations():
    """'[summary]'

    Returns:
        [type]: [description]
    """
    if request.method == 'POST':
        deletions_list = request.form.getlist('selection')
        print(deletions_list)
        cite_repo().delete_selected_citations(deletions_list)
            

    #message if database citation fails or succeeds

    return redirect("/citations")


@app.route("/citations.bib")
def show_bib_file():
    """
    A page for displaying citations in a form
    that can be saved as a .bib file
    """
    citations = cite_repo().list_citations()

    selection = request.cookies.get("selection").split(",")
    citations = cite_service().filter_to_selected(citations, selection)

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
        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
            types_list = []
            for entry_type in data:
                types_list.append(entry_type)
            return render_template("newcitation.html", list = types_list)

    entry_type = request.form.get("entry_type")
    return new_type(entry_type)


@app.route("/new/<entry_type>")
def new_type(entry_type):
    """
    A page for selecting the field types of the selected entry type.
    The available entry types and their possible field types can be found in data.json.
    """
    types_list = get_list_of_field_types(entry_type)
    return render_template("entrytypecitation.html", entry_type = entry_type, list = types_list, noerror = True)

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

    try:
        if cite_serve.validate(citation):
            cite_repo().store_citation(citation)
            return redirect("/new")
    except Exception as user_error:
        types_list = get_list_of_field_types(entry_type)
        return render_template("entrytypecitation.html", entry_type = entry_type, list = types_list, error = user_error,
        cite_as = cite_as, fields = fields)
    return redirect("/new")

def get_list_of_field_types(entry_type):
    """
    Generates the field types of a given entry type
    """
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
        if not entry_type in data:
            return redirect("/new")
        types_list = tuple(data[entry_type].items())
        return types_list
