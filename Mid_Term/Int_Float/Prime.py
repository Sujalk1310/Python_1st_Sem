n = int(input("Enter No. : "))
f = 0
for i in range (2,n):
	if n%i == 0 :
		f = 1
if f == 0 :
	print ("No. is Prime")
else :
	print ("No. is Composite")
