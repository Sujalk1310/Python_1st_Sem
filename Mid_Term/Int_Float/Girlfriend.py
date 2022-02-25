x = int(input("Enter Girl's House Co-ordinates : "))
if (x-0 >= 0 and type(x) == int ):
	Five = x//5
	Cond1 = x - (Five*5)
	Four = Cond1//4
	Cond2 = Cond1 - (Four*4)
	Three = Cond2//3
	Cond3 = Cond2 - (Three*3)
	Two = Cond3//2
	Cond4 = Cond3 - (Two*2)
	One = Cond4
	R = Five+Four+Three+Two+One
	print ("Steps to be taken : ",R)
else :
	print ("Invalid Input Value")
