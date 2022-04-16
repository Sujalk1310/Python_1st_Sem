n = int(input())
for i in range(0,n):
    R1 = 0
    R2 = 0
    Z = 0
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    if X < 0 and Y < 0 :
        Z = X*(-1)-Y*(-1)
    elif X < 0  :
        Z = Y+X*(-1)
    else :
        Z = Y - X
    R2 = Z//2
    if Z%2 != 0 :
        R1 = 2
    print (R2+R1)
        
        
