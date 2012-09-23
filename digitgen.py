x = raw_input('Please input digit in range [0-9]\n')

T = ('********\n*      *\n*      *\n*      *\n*      *\n*      *\n*      *\n********', '       *\n       *\n       *\n       *\n       *\n       *\n       *\n       *\n','********\n       *\n       *\n********\n*       \n*       \n*       \n********\n','********\n       *\n       *\n********\n       *\n       *\n       *\n********\n','*      *\n*      *\n*      *\n********\n       *\n       *\n       *\n       *\n','********\n*       \n*       \n********\n       *\n       *\n       *\n********\n','********\n*       \n*       \n********\n*      *\n*      *\n*      *\n********\n','********\n      * \n     *  \n    *   \n   *    \n  *     \n *      \n*       \n','********\n*      *\n*      *\n********\n*      *\n*      *\n*      *\n********\n','********\n*      *\n*      *\n********\n       *\n       *\n       *\n********\n')

try:

	if int(x) == 0:
		print "\n\n" + T[0]
	elif int(x) == 1:
		print "\n\n" + T[1]
	elif int(x) == 2:
		print "\n\n" + T[2]
	elif int(x) == 3:
		print "\n\n" + T[3]
	elif int(x) == 4:
		print "\n\n" + T[4]
	elif int(x) == 5:
		print "\n\n" + T[5]
	elif int(x) == 6:
		print "\n\n" + T[6]
	elif int(x) == 7:
		print "\n\n" + T[7]
	elif int(x) == 8:
		print "\n\n" + T[8]
	elif int(x) == 9:
		print "\n\n" + T[9]
	else:
		print "Input Incorrect!!!"

except:
	print "Input Incorrect!!!"
