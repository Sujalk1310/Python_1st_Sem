s1 = input()
s2 = input()
for i in s1:
    for j in s2 :
        if j not in s1 :
            s1 += j
        
    
print (s1)
