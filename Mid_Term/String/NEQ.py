n = input()
i = int(input())
if len(n)%2 == 0:
    l = len(n)//i
else :
    l = (len(n)//i)+1
for j in range (0,len(n),l):    
    print(n[j:j+l])
