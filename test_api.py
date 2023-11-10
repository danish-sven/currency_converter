import unittest
import requests
import datetime
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_function(self):
        # Testing to confirm 'OK' status codes for URLs
        # status code 200 shows correct URL
        # format_currencies_url
        # format_latest_url

        host_url = _HOST_
        currencies_url = format_currencies_url()
        latest_url = _HOST_ + _LATEST_
        exchange_url = format_latest_url('AUD')
    
        host_response = requests.get(host_url)
        currencies_response = requests.get(currencies_url)
        latest_response = requests.get(latest_url)
        exchange_response = requests.get(exchange_url)

        #Seems redundant.. but I feel like it's a basic check anyway
        self.assertEqual(host_url, _HOST_)
        self.assertEqual(currencies_url, _HOST_ + _CURRENCIES_)
        self.assertEqual(latest_url, _HOST_ + _LATEST_)
        self.assertEqual(exchange_url, _HOST_ + _LATEST_ +"?from="+"AUD" )

        #Status 200 shows URL is correct
        self.assertEqual(host_response.status_code, 200)
        self.assertEqual(currencies_response.status_code, 200)
        self.assertEqual(latest_response.status_code, 200)
        self.assertEqual(exchange_response.status_code, 200)



class TestAPI(unittest.TestCase):
    def test_function(self):
        # Testing call_api function. If returns empty dictionary, then error
        # get_currencies

        #Test to see if API returns empty dictionary
        exchange_url = format_latest_url('AUD')
        test = call_api(exchange_url)
        test = bool(test)

        #Load latest results
        latest_url = _HOST_ + _LATEST_
        latest_response = requests.get(latest_url)
        latest_dict = latest_response.json()

        #confirm the latest date - frankfurter doesn't appear to update on weekends
        today = datetime.date.today()
        if today.weekday() == 0:
            test_date = today - datetime.timedelta(days=3)
            test_date = str(test_date)
        elif today.weekday() == 6:
            test_date = today - datetime.timedelta(days=2)
            test_date = str(test_date)
        elif today.weekday() == 5:
            test_date = today - datetime.timedelta(days=1)
            test_date = str(test_date)
        else:
            test_date = today
            test_date = str(test_date)

        # Confirming that all rates are numbers and that none of them are zero
        rates = latest_dict.get('rates')
        allnum = all(isinstance(i,(float,int)) for i in list(rates.values()))
        nozero = any(i != 0 for i in list(rates.values()))

        #Load Currency results
        currencies_url = _HOST_ + _CURRENCIES_
        currency_response = requests.get(currencies_url)
        currency_dict = currency_response.json()

        #Confirm they're all strings
        allstringkeys = all(isinstance((i),str) for i in list(currency_dict.keys()))
        allstringvalues = all(isinstance((i),str) for i in list(currency_dict.values()))

        #check if get_currencies function returns list of keys and that the keys are all 3 letters and uppercase
        currency_list = get_currencies()
        goodlength = all(True if len(i) == 3 else False for i in currency_list)
        goodupper = all(True if i.isupper() else False for i in currency_list)

        #If api call went through correctly, the dictionary will not be empty
        self.assertEqual(test, True)

        #Test Latest
        self.assertEqual(latest_dict.get('amount'), 1.0)
        self.assertEqual(latest_dict.get('base'), "EUR")
        self.assertEqual(latest_dict.get('date'), test_date)
        self.assertEqual(allnum, True)
        self.assertEqual(nozero, True)
        
        #Test Currency
        self.assertEqual(allstringkeys, True)
        self.assertEqual(allstringvalues, True)
        self.assertEqual(goodlength, True)
        self.assertEqual(goodupper, True)


if __name__ == '__main__':
    unittest.main()