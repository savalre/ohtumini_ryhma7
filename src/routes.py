"""
Routes module for flask app
Used by app.py
"""
from flask import render_template, redirect, request
from app import app
from entities.citation import Citation
from entities.types import Types
#Will be needed in future
#from flask import redirect, session, request, url_for
from repositories.citation_repository import CitationRepository as cite_repo

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

@app.route("/new", methods=["POST", "GET"])
def new():
    """
    A page for selecting an entry type
    """
    if request.method == "GET":
        return render_template("newcitation.html")
    else:
        entry_type = request.form.get("entry_type")
        return new_type(entry_type)


@app.route("/new/<entry_type>")
def new_type(entry_type):
    """
    A page for selecting the field types of the selected entry type
    """
    if entry_type not in Types().entry_types:
        return redirect("/new")
    func = getattr(Types(), entry_type)
    list = func()
    return render_template("entrytypecitation.html", entry_type = entry_type, list = list)

@app.route("/new/citation", methods=["POST", "GET"])
def new_citation():
    """
    Functionality for adding a new citation after receving the values from the correct form.
    If the citation is valid, it is stored in the database.
    """
    if request.method == "GET":
        return redirect("/new")
    else:
        fields = []
        entry_type = request.form.get("entry_type")
        cite_as = request.form.get("cite_as")

        for field_name in request.form:
            value = request.form.get(field_name)
            if value and field_name != "cite_as" and field_name != "entry_type":
                fields.append((field_name, value))

        citation = Citation(cite_as, entry_type, fields)
        # validate citation
        cite_repo().store_citation(0, citation)
        return redirect("/new")
