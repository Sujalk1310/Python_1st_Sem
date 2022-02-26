st = input().split()
ls = []
for i in range(0,len(st)):
    ls.append(st[i])
for i in ls:
    if len(ls[i]) < len(ls[i+1]) :
        l = ls[i]
print (l)
