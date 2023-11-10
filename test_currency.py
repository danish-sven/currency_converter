import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    # Setup a custom self, with nested dictionaries to match my function's flow. 
    def setUp(self):
        self.from_currency: str = 'AUD'
        self.to_currency: str = 'USD'
        self.amount: float = 1.0
        self.rate: dict = {'USD':0.7}
        self.inverse_rate: dict = {'AUD':1.3}
        self.date: str = '2021-09-03'
        
    def test_function(self):
        # My data is a custom dictionary which is a combination of the rate as well as the inverse rate
        data = {
            'base' : self.from_currency,
            'to' : self.to_currency,
            'amount' : self.amount,
            'rates' : self.rate,
            'inverse' : self.inverse_rate,
            'date' : self.date
                }

        currency = Currency()
        currency = extract_api_result(data)
        
        self.assertEqual(currency.from_currency, self.from_currency)
        self.assertEqual(currency.to_currency, self.to_currency)
        self.assertEqual(currency.amount, self.amount)
        self.assertEqual(currency.rate, self.rate.get('USD'))
        self.assertEqual(currency.inverse_rate, self.inverse_rate.get('AUD'))
        self.assertEqual(currency.date, self.date)
        


class TestExtractApi(unittest.TestCase):
    def test_function(self):

        data = ['AUD','USD']
        bad = ['NOPE','NOTGOOD']
        same = ['AUD','AUD']
        empty = []
        bonus = ['AUD','USD','GBP']
        CURRENCIES = ['AUD','USD','GBP']

        # I did a lot of the checking in main.py - in the interesting of testing all of my code, I will include it here

        def clean_codes(args):
            if len(args) != 2: #In the actual function this test is 3 becase it relies on sys.argv which will be 3 including 'main.py'
                #print(f"[ERROR] Please provide two currency codes from this list: \n{CURRENCIES}")
                return False
            else:
                args = [i.upper() for i in args] #make sure they're uppercase
                if args[0] == args[1]:
                    # print(f'[ERROR] You did not provide two different currency codes. Please choose two different currency codes from this list: \n{CURRENCIES}')
                    # return None
                    return False
                elif check_valid_currency(args) == False:
                    # print(f'[ERROR] {args} is not a valid option. Please choose two valid currency codes from this list: \n{CURRENCIES}')
                    # return None
                    return False
                else:
                    return True
        
        valid = clean_codes(data)
        invalid = clean_codes(bad)
        samesame = clean_codes(same)
        void = clean_codes(empty)
        toomuch = clean_codes(bonus)

        self.assertEqual(valid, True)
        self.assertEqual(invalid, False)
        self.assertEqual(samesame, False)
        self.assertEqual(void, False)
        self.assertEqual(toomuch, False)

if __name__ == '__main__':
    unittest.main()