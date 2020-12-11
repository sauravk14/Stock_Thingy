#Company Directory
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

preferences = dict()
ppl_to_prefs = dict()

def fill_pref(name):
    for k, v in symbo_dict:
        preferences[v] = input(f'Are you bearish or bullish on {k}? Pls type "bear" or "bull". ')
    ppl_to_prefs[name] = preferences

def main():
    name = input('What is your Name? ')
    fill_pref(name)

main()