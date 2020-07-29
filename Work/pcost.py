# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):

	total_cost = 0.0

	import csv
	f = open(filename)
	rows = csv.reader(f)
	headers = next(rows)

	#print(headers)

	for row in rows:
		#print(row)
		try:
			total_cost = total_cost + int(row[1]) * float(row[2])
		except ValueError:
			print("Couldn't parse", row)

	return total_cost

if len(sys.argv) == 2:
	print(sys.argv[1])
	filename = sys.argv[1]
else:
	filename = r'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost =', cost)