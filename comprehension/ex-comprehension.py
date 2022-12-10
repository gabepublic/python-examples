
print("\nSquare ======================")
#~~~~~~
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
#~~~~~~
print(squares)


import csv
f = open('comprehension/data.csv', 'r')
rows = csv.reader(f)
header = next(f)    # skip the header line
#~~~~~~
col1 = [row[0] for row in rows]
#~~~~~~
print("\nColumn-1======================")
print(col1)

f.seek(0)       # reset the cursor to the start of the file
header = next(f)    # skip the header line
#~~~~~~
greaterThan5 = [row[2] for row in rows if int(row[2]) > 5]
#~~~~~~
print("\nColumn-3 > 5======================")
print(greaterThan5)


# ZIP - combine two lists; instead of using two loops
print("\n zip ======================")
tickers = ['GOOGL', 'AAPL', 'YHOO', 'COST']
names = ['Google', 'Apple', 'Yahoo', 'Costco']
for ticker, name in zip(tickers, names):
    print(ticker, '=', name)

# ZIP to create dictionary
company_ticker = dict(zip(names, tickers))
print(company_ticker)

# Filtered list of tuples
print("\n filtered list of tuples=======================")
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()
cards = [Card(rank, suit) for suit in suits
                          for rank in ranks]
print('Cards: ', cards)
print('Reversed cards: ', reversed(cards))
print('Total cards: ', len(cards))
filtered = [tup for tup in cards if tup[1] == 'spades']
print('Filtered all spades: ', filtered)
print('Total spades: ', len(filtered))

from random import choice
print('Random draw: ', choice(cards))

print('Is 2-hearts in filtered cards: ', Card('2', 'hearts') in filtered)
print('Is 3-spades in filtered cards: ', Card('2', 'spades') in filtered)