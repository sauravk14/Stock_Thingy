import yfinance as yf
from pprint import pprint

#name & price dict
stag = {"name": None,
        "price": None}

#name to symbol dict
symbo_dict = dict()
symbo_dict['Apple'] = 'AAPL'
symbo_dict['Microsoft'] = 'MSFT'
symbo_dict['Tesla'] = 'TSLA'
symbo_dict['Alphabet'] = 'GOOGL'
symbo_dict['Amazon'] = 'AMZN'
symbo_dict['Disney'] = 'DIS'
symbo_dict['Facebook'] = 'FB'
symbo_dict['Twitter'] = 'TWTR'
symbo_dict['Delta'] = 'DAL'
symbo_dict['Nike'] = 'NKE'
symbo_dict['AMD'] = 'AMD'
symbo_dict['Intel'] = 'INTC'
symbo_dict['Boeing'] = 'BA'
symbo_dict['Target'] = 'TGT'
symbo_dict['Visa'] = 'V'

#getting stock tag with name and price values
def get_stag(stock):
    a = yf.Ticker(stock)
    return {"name": a.info.get('longName'),
            "price": a.info.get('ask')}

#Turn a Typed Name into Ticker Symbol for API
def name_to_sym(name):
    return symbo_dict.get(name)

# Some Dictionary Python Syntax For Myself
# Ayush Ignore This
#{
#    "name": stock_name,
#    "price": stock_price
#}
#stag['name'] = "MSFT",
#stag['price'] = 130.2

#Filteres Dictionary to Send to Ayush
my_struct = dict()

#Given Ticker Symbol, Get Official Name
def get_sname(stock):
    a = yf.Ticker(stock)
    return a.info.get('longName')

#Given Ticker Symbol, Get Current Price
def get_sprice(stock):
    a = yf.Ticker(stock)
    return a.info.get('ask')
    #that ask is prob wrong. Unsure what exact real time price variable in API is

def main():
    q = input('What company are you looking for? ')
    while q != 'Done':
        c_sym = name_to_sym(q)
        if c_sym is None:
            print('Not in Existence')
        else:
            print(get_stag(c_sym))
        q = input('What company are you looking for? If finished, type "Done". ')

main()