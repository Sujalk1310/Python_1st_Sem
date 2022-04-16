st = str(input())
l = len(st)
k = int(input())
while k >= l :
    k = k-l
if k-l == 0 :
    print(st[k:])
else :
    print(st[k:],st[0:k],end="",sep="")
