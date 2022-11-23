import csv
f = open('datastruc/data.csv', 'r')
rows = csv.reader(f)
header = next(f)    # skip the header line
stocks = []
for ticker, name, date, price in rows:
    rec_dict = {
        'ticker': ticker,
        'name': name,
        'date': date,
        'price': float(price)
    }
    stocks.append(rec_dict)
print("original stock list:")
print(stocks)

################################
# SORT - using helper function

def ticker_name(stock):
    return stock['ticker']

stocks.sort(key=ticker_name)
print("sorted stock list - ticker:")
print(stocks)

################################
# SORT - using LAMBDA function
stocks.sort(key=lambda stock: stock['price'])
print("sorted stock list - price:")
print(stocks)
f.close()

################################
# GROUPING - using LAMBDA function
# ASSUMPTION: the list must be sorted first

f = open('datastruc/data-dupe.csv', 'r')
rows = csv.reader(f)
header = next(f)    # skip the header line
stocks = []
for ticker, name, fdate, pdate, price in rows:
    rec_dict = {
        'ticker': ticker,
        'name': name,
        'fdate': fdate,
        'pdate': pdate,
        'price': float(price)
    }
    stocks.append(rec_dict)
print("original stock list - dupe:")
print(stocks)

stocks.sort(key=lambda stock: stock['ticker'])
print("sorted stock list - ticker:")
print(stocks)

import itertools
stocks_grouped = itertools.groupby(stocks, key=lambda stock: stock['ticker'])
print("grouped stock list - ticker:")
#print(stocks_grouped)
for ticker, items in itertools.groupby(stocks, lambda stock: stock['ticker']):
    print(ticker)
    for item in items:
        print('    ',item)
