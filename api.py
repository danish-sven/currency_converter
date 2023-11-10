import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response or an error message

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    Run the API 'GET' call
    if response from API is successful:
        output received JSON as dictionary
    else:
        print error message

    Returns
    -------
    requests.models.Response
        Response from API request or error message
        If code 200, will return dictionary of results
    """
    resp = requests.get(url)
    if resp.status_code == 200:
        resp_dict = resp.json()
        return resp_dict
    else:
        print('[ERROR] There was an error with the API call')
        return {}

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    Combine the URL strings to specify the currencies list from Frankfurter app

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    url = _HOST_ + _CURRENCIES_
    return url


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    Get currencies list from Frankfurter app
    Extract the keys from the dictionary that was returned from the Frankfurter's list of currencies as a list

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    
    currency_list = list(call_api(format_currencies_url()).keys())
    return currency_list


def format_latest_url(currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    Format the URL for the API request to specify the latest currency exchange rate

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    url = _HOST_ + _LATEST_ +"?from="+currency 
    return url