n = int(input("Enter No. : "))
c = 0
sum = 0
tm = n
while n != 0:
	n = n//10
	c += 1
n  = tm
while n != 0:
	d = n%10
	n = n//10
	sum += d**c
	
if sum == tm :
	print ("No. is Armstrong")
else :
	print ("No. is Not Armstrong")
