# read raw data
f = open('file/data.csv', 'r')
data = f.read()
print(data)
f.close()
print("**********")

################
# Better coding
################
with open('file/data.csv', 'r') as f:
    header = next(f)    # skip the header line
    for line in f:
        print(line)
print("**********")
        
###################
# Using csv module 
###################
import csv
f = open('file/data.csv', 'r')
rows = csv.reader(f)
header = next(rows)
for row in rows:
    # convert to int and multiple by 2
    # if not convert to int first, the result is duplicate string
    row[1] = 2*int(row[1])
    print(row)
f.close()
