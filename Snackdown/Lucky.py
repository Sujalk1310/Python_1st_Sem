n = int(input())
list = []
for i in range (0,n):
    f = 0
    a = input().split()
    for j in range (0,3):
        b = str(a[j])
        if int(b) == 7 :
            f = 1
    if f == 1 :
        list.append("YES")
    else :
        list.append("NO")
for i in range (0,n):
    print (list[i])
    
