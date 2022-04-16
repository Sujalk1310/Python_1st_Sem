n = int(input())
l = []
e = input().split()
for k in range (0,n):
    l.append(int(e[k]))
for j in range (0,n):
    if l[j]%2==0:
        l[j] = 0
    else :
        l[j] = 1
for i in range (0,n):
    print (l[i],end = " ")
