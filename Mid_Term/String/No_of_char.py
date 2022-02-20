n = "hello python world"
m = ""
z = ""
for i in range (0,len(n)):
    z += n[i]
    if z not in m :
        m += z
        z = ""
    else :
        z = ""
for i in m :
    out = n.count(i)
    if out >= 2 :
        print (i)

