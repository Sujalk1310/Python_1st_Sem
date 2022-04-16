n = int(input())
list = []
for i in range (0,n):
    I = 0
    E = 0
    a = input().split()
    for j in range (0,5) :
        b = int(a[j])
        if  b == 1 :
            I += 1
        elif b == 2 :
            E += 1
    if I-E == 0:
        list.append("DRAW")
    elif I-E >= 1 :
        list.append("INDIA")
    else :
        list.append("ENGLAND")
for i in range (0,n):
    print (list[i])

        
            
