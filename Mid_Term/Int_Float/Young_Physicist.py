n = int(input())
x = 0
y = 0
z = 0
for i in range (0,n) :
    k = input().split()
    x += int(k[0])
    y += int(k[1])
    z += int(k[2])
if x == 0 and y == 0 and z == 0 :
    print ("YES")
else :
    print ("NO")
    
    
