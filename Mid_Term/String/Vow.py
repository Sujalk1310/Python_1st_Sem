st = input()
st = st.lower()
D = 0
C = 0
W = 0
V = 0
l = len(st)
for i in range (0,l):
	for j in range (48,58) :
		if st[i] == chr(j) :
			D += 1
	for k in range (97,122):
		if st[i] == chr(k):
			if st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u' :
				V +=1
			else :
				C += 1
	if st[i] == " " :
		W += 1
print ("Vowels :",V)
print ("Consonant :",C)
print ("Digit :",D)
print ("Whitespace :",W)
	
