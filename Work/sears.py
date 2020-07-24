bill_thickness = 0.11 #mm
no_of_bills = 1
total_no_of_bills = 1
sears_height = 442 * 1000 #mm
days = 1

print('day ', 'no_of_bills ', 'total_no_of_bills ', 'bill_thickness ')


while (bill_thickness * total_no_of_bills < sears_height):
	print(days, no_of_bills, total_no_of_bills, bill_thickness * total_no_of_bills / 1000)
	days = days + 1
	no_of_bills = no_of_bills * 2 #adding double of prev day
	total_no_of_bills = total_no_of_bills + no_of_bills #stack of bills count
	

print('days = ', days)
print('total_no_of_bills = ', total_no_of_bills)
print('total thickness = ', bill_thickness * total_no_of_bills / 1000)