# A simple example of if..... elif..... ladder


x = int(input("Please enter a number: "))

if x<0:
	x = 0
	print('Negative changed to zero')
	
elif x == 0:
	print('Zero')
	
elif x == 1:
	print('Single')
	
else:
	print('More')
