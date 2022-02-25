n = str(input("Enter Value : "))
l = len(n)
sum = 0
for i in range (0,l):
	sum += int(n[i])**l
if sum == int(n) :
	print("No. is Armstrong")
else :
	print("No. is Not Armstrong")
	
