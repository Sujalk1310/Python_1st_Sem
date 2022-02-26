QS = []
f = 0
g = 0
while f == 0 :
	c = str(input("Do you want to add ? (Y/N)"))
	if c == 'n' or c == 'N' :
		f = 1
	elif c == 'y' or c == 'Y' :
		v = str(input("Enter String : "))
		QS.append(v)
		g += 1
	else :
		print ("Invalid Input")
S = str(input("Search Query : "))
if g != 0 :
	for i in QS :
		SQS = i.lower()
		SS = S.lower()
		if SQS.startswith(SS) :
			print (i)
else :
	print ("List Empty")
	

