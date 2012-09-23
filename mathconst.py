x = raw_input('Input constant and accuracy, example pi:5 \nAvailable constants is E, PI and LN10 \nMax accyracy 12 digits\n').lower()
z = x.split(':')

d = { "pi":"3.141593265357",
	"e":"2.718281828459",
	"ln10":"2.301232130132" }


try:
	if len(z) > 2:
		2/0
	n = d[z[0]].split('.')
	print n[0] + "." + n[1][:int(z[1])]
except:
	print "Incorrect input or constant not found"


