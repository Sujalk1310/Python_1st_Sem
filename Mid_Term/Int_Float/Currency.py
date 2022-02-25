n = int(input("Enter Value"))
if (n>=100):
	x = n-100
	TTR =  x//2000
	Cond1 = x-(TTR *2000)
	FHR = Cond1//500
	Cond2 = Cond1-(FHR*500)
	OHR = Cond2//100
	print ("No. of 100 Notes :",OHR+1)
	print ("No. of 500 Notes :",FHR)
	print ("No. of 2000 Notes :",TTR)
else :
	print ("Money Cannot be Withdrawn")

