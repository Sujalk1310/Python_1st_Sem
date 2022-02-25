AB = float(input("Enter Side AB :"))
BC = float(input("Enter Side BC :"))
CA = float(input("Enter Side CA :"))
Cond1 = ((AB**2)+(BC**2))**(1/2)
Cond2 = ((BC**2)+(CA**2))**(1/2)
Cond3 = ((CA**2)+(AB**2))**(1/2)
S = (AB+BC+CA)/2
Cond4 = (S*(S-AB)*(S-BC)*(S-CA))**(1/2)
if ( Cond4 != 0): 
	if ( AB != BC and BC != CA ):
		x = "Triangle is SCALAR"
	elif ( AB == BC and BC == CA ):
		x = "Triangle is EQUILATERAL"
	elif ( AB == BC or BC == CA ):
		x = "Triangle is ISCOCELES"
		if (Cond1 == CA or Cond2 == AB or Cond3 == BC ):
			x = "Triangle is RIGHT-ANGLED ISOCELES"
	elif ( Cond1 == CA or Cond2 == AB or Cond3 == BC ):
		x = "Triangle is RIGHT-ANGLED"
	else :
		print ("Cannot Determine the Triangle Type")
	print (x)
else :
	print ("Invalid Triangle Parameters")

