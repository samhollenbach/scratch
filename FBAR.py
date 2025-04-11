import csv

"""
Calculate the current and max balance of a bank account, provided a transactions list
"""

FILE = '/Users/samhollenbach/Downloads/9e482e55-dd49-44fd-b12a-c00cb98b5625.csv'


bal = 0
max_bal = 0

with open(FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        diff = float(row['Amount (EUR)'])
        bal += diff
        max_bal = max(max_bal, bal)
print(f'End Balance: {bal} EUR')
print(f'Max Balance: {max_bal} EUR')