# mortgage.py
#
# Exercise 1.7
principal_balance = 500000
rate = 0.05 #5%
time = 30 #years
monthly_payment = 2684.11
year = 1 #init
cumulative_interest_paid = 0
month_counter = 0;
month_counter_for_annual_reset = 0 #reset at 12
annual_interest_paid = 0 
annual_principal_paid = 0
total_paid = 0
number_of_payments = 0
#extra_payment_counter = 12 #count down to 0
extra_payment_start_month = int(input('extra_payment_start_month: '))
extra_payment_end_month = int(input('extra_payment_end_month: '))
extra_payment_input = int(input('extra_payment: '))

#print('year', 'principal_paid', 'principal_balance', 'interest_paid', 'cumulative_interest_paid')

print('month', 'total_paid', 'principal_balance')

while principal_balance > 0:
	month_counter = month_counter + 1
	monthly_interest = rate/12 * principal_balance

	if((principal_balance + monthly_interest) < monthly_payment): #last payment
		principal_paid = principal_balance
		total_paid = total_paid + principal_balance + monthly_interest
		principal_balance = 0	
	else:
		if((month_counter >= extra_payment_start_month) and 
		  (month_counter <= extra_payment_end_month)):
			extra_payment = extra_payment_input
		else:
			extra_payment = 0
			#extra_payment_counter = extra_payment_counter - 1

		principal_paid = monthly_payment - monthly_interest + extra_payment
		principal_balance = principal_balance - principal_paid
		total_paid = total_paid + monthly_payment + extra_payment

	print(month_counter, round(total_paid), round(principal_balance))

	annual_interest_paid = annual_interest_paid + monthly_interest
	annual_principal_paid = annual_principal_paid + principal_paid
	number_of_payments = number_of_payments + 1
	month_counter_for_annual_reset = month_counter_for_annual_reset + 1

	if(month_counter_for_annual_reset == 12):
		cumulative_interest_paid = cumulative_interest_paid + annual_interest_paid
		print('#year', year, round(annual_principal_paid), round(principal_balance), 
			round(annual_interest_paid), round(cumulative_interest_paid), '#')
		year = year + 1
		annual_interest_paid = 0 #reset
		annual_principal_paid = 0 #reset
		month_counter_for_annual_reset = 0; #reset

print('Number of payments', number_of_payments)
print('Total paid', round(total_paid))
