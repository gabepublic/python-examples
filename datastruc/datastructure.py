################################
# TUPLES; is a record that can store various types 
# IMMUTABLE
t = ('AAPL', 'Apple Inc', '1976-04-11', 2.378)
print(t[0], ' - ', t[1])

# unpacking tuple
ticker, name, foundedDate, marketCapBillion = t
print(ticker, ' - ', name)
print('=================')


################################
# LIST; typically contains same type
# MUTABLE

tickers = ['IBM', 'AAPL', 'YHOO', 'VOO']

# modify the list
tickers.append('GOOGL')
print(tickers)
tickers[0] = 'AMZN'
print(tickers)
print('=================')

################################
# SET; contains UNIQUE values
# IMMUTABLE
day_of_week = {'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'}


# convert list to set; all duplicates will be truncated
#set(list_contains_duplicate)

# in - to check existence
exist = 'MON' in day_of_week
print("Mon is the day of the week: ", exist)
print('=================')

################################
# DICT; mapping key-values
# MUTABLE
prices = {'AMZN': 93.10, 'AAPL': 150.03, 'GOOG': 97.24}
print("current stock price of AMZN: ", prices['AMZN'])

# create a list of dictionary and dump it into JSON
import csv
f = open('datastruc/data.csv', 'r')
rows = csv.reader(f)
header = next(f)    # skip the header line
stocks_list = []
for ticker, name, date, price in rows:
    rec_dict = {
        'ticker': ticker,
        'name': name,
        'date': date,
        'price': price
    }
    stocks_list.append(rec_dict)
print(stocks_list)

import json
stocks_json = json.dumps(stocks_list)
print(stocks_json)