import sys

from requests import NullHandler
from currency import check_valid_currency, CURRENCIES, extract_api_result, call_api, format_latest_url
from api import format_latest_url

def main():
    """
    Function that will check if there are two valid arguments provided.
    If so it will return get the conversion rates
    If not it will print an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    if there are only two arguments:
        make uppercase
        if two arguments don't equal each other:
            if currency is valid:
                get conversion rates

    Returns
    -------
    str
        Formatted API result or error message
    """
    # Get the system arguments
    args = sys.argv[1:3]

    # Check there are only two currencies - can add more later
    if len(sys.argv) != 3:
        print(f"[ERROR] Please provide two currency codes from this list: \n{CURRENCIES}")
    else:
        args = [i.upper() for i in args] #make sure they're uppercase
        if args[0] == args[1]:
            print(f'[ERROR] You did not provide two different currency codes. Please choose two different currency codes from this list: \n{CURRENCIES}')
            return None
        elif check_valid_currency(args) == False:
            print(f'[ERROR] {args} is not a valid option. Please choose two valid currency codes from this list: \n{CURRENCIES}')
            return None
        else:
            get_rate(args[0],args[1])


def get_rate(from_currency: str, to_currency: str):
    """
    Function will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    Create a dictionary from JSON from API call of 'from_currency'
    add an element in dictionary from 'to_currency'
    run GET on 'to_currency' and pull out the conversion rate to the 'from_currency' as the inverse rate
    extract key parts of resulting dictionary
    format results

    Returns
    -------
    str
        Formatted API result
    """
    rate_dict = call_api(format_latest_url(from_currency))
    rate_dict['to'] = to_currency

    inverse_rates = call_api(format_latest_url(to_currency))
    rate_dict['inverse'] = inverse_rates.get('rates')

    result = extract_api_result(rate_dict)
    result.format_result(result)


if __name__ == "__main__":
    main()