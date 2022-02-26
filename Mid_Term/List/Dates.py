k = int(input())
s = 0
f = 0
list = []
while f != k :
    s += 1
    ss = str(s)
    g = ss[-1]
    if s%3 == 0 and int(g) == 3 :
        d = 0
    elif s%3 == 0 or int(g) == 3 :
        d = 0
    else :
        d = 1
    if d == 1 :
        list.append(s)
        f += 1
    
print(list[k-1])

    


        
    
