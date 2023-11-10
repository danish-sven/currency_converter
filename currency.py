from api import call_api, format_latest_url, get_currencies
from dataclasses import dataclass

CURRENCIES = get_currencies()

def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    Check if the currency code provided by the user is in the list provided by Frankfurter:

    if system argument is valid currency in list:
        return true
    else:
        return false

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    if all(x in CURRENCIES for x in currency):
        return True
    else:
        return False


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Description of `attr2`.
    """

    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        print(f"{self.date} - Today's conversion rate from {self.from_currency} to {self.to_currency} is {self.rate}. The inverse rate ({self.to_currency} to {self.from_currency}) is {self.inverse_rate}.")

        return None


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Currency code to be converted from as well as currency code to be converted to

    Pseudo-code
    ----------
    Take dictionary with combined to/from JSON results 
    instantiate currency class
    assign elements to currency class

    Returns
    -------
    Currency
        Instantiated Currency with filled in results
    """
    rates = result.get('rates')
    inverse = result.get('inverse')

    extracted_results = Currency

    extracted_results.from_currency = result.get('base')
    extracted_results.to_currency = result.get('to')
    extracted_results.date = result.get('date')
    extracted_results.amount = result.get('amount')
    extracted_results.rate = rates.get(result.get('to'))
    extracted_results.inverse_rate = inverse.get(result.get('base'))

    return extracted_results
