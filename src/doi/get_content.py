"""
Function to make a request to the ACM web library
"""
import json
import requests

def get_content(doi):
    """
    Makes a request to the ACM web library and returns the content
    of the request.

    Parameters:
        doi: doi number of the wanted article
    Returns:
        Contents of the request if the page exists,
        otherwise error.
    """
    url = "https://dl.acm.org/action/exportCiteProcCitation"
    params = {"dois":doi,
              "targetFile": "custom-bibtex",
              "format": "bibTex"
             }
    response = requests.get(url, params, timeout=10)
    try:
        data = json.loads(response.text)
        items = data['items']
        article = items[0]
        content = article[doi]
        return content
    except json.JSONDecodeError:
        return "404"
