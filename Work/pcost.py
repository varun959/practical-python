# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open(r'Data/portfolio.csv', 'rt') as f:
	next(f) #skip header
	for line in f:
		row = line.split(',')
		total_cost = total_cost + int(row[1]) * float(row[2])

print('Total cost =', total_cost)