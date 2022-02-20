st = input()
x = ''
l = len(st)

for i in range (0,l):
	for j in range (97,123):
		if st[i] == chr(j) :
			x += chr(j) 
print (x)
