"""
Function to make a request to the ACM web library
"""
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
    url = f"https://dl.acm.org/doi/{doi}"
    req = requests.get(url, timeout=10)
    if req.status_code == 404:
        return "404"
    return req.content
