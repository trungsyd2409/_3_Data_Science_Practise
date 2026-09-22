import requests

REQUEST_TIMEOUT = 10  # seconds


def get_url(url: str) -> tuple[int, str]:
    """
    Function that will call a provided GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return 500, f"Error occurred while calling the API endpoint: {e}"
