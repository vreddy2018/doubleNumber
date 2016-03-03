
Number = 0

while Number == 0:
	userNumber = raw_input("Number: ")
	try:
		Number = float(userNumber)
		
		#Only put that you expect to cause exceptions here
	except ValueError:
		print('not number')


print('Double is {}'.format(Number*2))