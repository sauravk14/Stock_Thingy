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

#a person's preference on each stock
preferences = dict()

#all persons' preferences collection
ppl_to_prefs = dict()

#fills a person's preferences dict
#then adds the person and their preferences to the main dict
def fill_pref(name):


    for k, v in symbo_dict.items():
        #TODO: add logic to make sure they can only enter "bear" or "bull".
        a = input(f'Are you bearish or bullish on {k}? Pls type "bear" or "bull": ')
        if (a == 'bull') or (a == 'bear'):
            preferences[v] = a
        else:
            Exception('Not Readable')
    ppl_to_prefs[name] = preferences


def main():
    name = input('What is the first persons name? ')
    while name != 'Done':
        fill_pref(name)
        name = input('What is the next persons name? If finished, type "Done".')

main()