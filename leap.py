def leap(x):

	if ((float(x) % 4) == 0 and (float(x) % 100) <> 0) or (float(x) % 400) == 0:
		print "Year " + str(x) + " is leap"

	else:
		print "Year " + str(x) + " not leap"

x = raw_input('Input year ')

try:
	int(x) or int(x)
except(TypeError, ValueError):
	print "Incorrect input"	
else:
	if int(x) < 0:
		print "Incorrect input"
	else:
		print leap(x)
