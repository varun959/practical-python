# bounce.py
#
# Exercise 1.5
num_bounce = 0
height = 100

print('bounce number', 'height')

while num_bounce != 10:
	num_bounce = num_bounce + 1
	height = round(height * 0.6, 4)
	print(num_bounce, height)