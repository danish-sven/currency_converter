<h1 align="center">Currency Converter App></h1>

## Author

Stefan Hall

- Student ID: 14156968
- Email: stefan.hall@student.uts.edu.au

## Description
The app is built for getting latest conversion rates for different international currencies.

## Available Commands

In the project directory, you can run:

### `python main.py AUD EUR`,

If you are using Pipenv, then you can run:

### `pipenv run python main.py AUD EUR`,

Please choose only two of the following currency codes:
['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

## Built With

- Python

## Package Dependencies

- requests
- datetime (for unit-testing)

## Structure

    ├── api.py  <- API handler. Specifies URLs for various requests from Frankfurter.app and               
    ├  		      returns JSON files with conversion numbers.
    ├───── call_api() - Function used to make API calls to the Frankfurter app
    ├───── format_currencies_url() - Function used for formatting the URL for the
    ├     						      ‘currency’ endpoint from the Frankfurter app
    ├───── get_currencies()- Function that will extract the list of available currencies from the 
    ├     					   Frankfurter app
    ├───── format_latest_url() - Function used for formatting the URL for the ‘latest’ endpoint from 
    ├  					      the Frankfurter app
    └──────────────────────────────────────────
    
    ├── currency.py        <- Extracts results from JSON and compares inputs to results. If inputs 
    ├					    match valid results, returns formatted message of conversion rates
    ├───── check_valid_currency() - Function that will check if a given currency code
    ├								belongs to the list of available currencies from the 
    ├	   							 Frankfurter app
    ├───── class Currency - Class defining the relevant information to be stored
    ├ 						as attributes, methods for calculating inverse rate
    ├ 						and formatting output
    ├───── extract_api_result() - Function that will read API output, instantiate a
    ├ 						Currency class and calculate the inverse rate
    └──────────────────────────────────────────

    ├── main.py            <- Input gateway. Tests if inputs meet validity conditions, if inputs are invalid, 
    ├					   prints error messages and suggests corrections. If inputs are correct, 
    ├					   runs functions which make API calls then run data extraction and returns
    ├					   printed message with currency conversion rates going both ways.
    
    ├───── main() - Function that checks if there is the correct number of arguements
    ├					and calls check_valid_currency before calling get_rate
    ├───── get_rate() - Function that extracts the conversion rate and formats the output
    └──────────────────────────────────────────
    
    ├── Pipfile            <- dedicated file used by the Pipenv virtual environment to manage project 
    ├				         dependencies
    └──────────────────────────────────────────
    
    ├── Pipfile.lock       <- Specifies the packages to be used for this application
    └──────────────────────────────────────────
    
    ├── README.md          <- Program description & author details.
    └──────────────────────────────────────────
    
    ├── test_api.py        <- Unit testing API functions. Runs multiple scenarios against functions and 
    ├					    predicts results.
    ├─────  TestFormatUrl - Class defining the unit tests for format_currencies_url and 
    ├ 						format_latest_url functions
    ├───── TestAPI - Class defining the unit tests for get_currencies and
    ├						call_api functions
    ├
    └──────────────────────────────────────────
    
    ├── test_currency.py   <- Unit testing currency functions as well as validity functions from 
    ├ 					main.py. Runs multiple scenarios against functions and predicts 
    ├ 					results.
    ├───── TestValidCurrency - Class defining the unit tests for check_valid_currency function
    ├───── TestExtractApi - Class defining the unit tests for extract_api_result function and 
    ├						  Currency class       
    └──────────────────────────────────────────
    
