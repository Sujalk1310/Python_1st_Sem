n = int(input())
for i in range (0,n) :
    x,y = input().split()
    x = int(x)
    y = int(y)
    z = x*y
    if x>z :
       g = x
       s = y
       i = x
       for j in range (x+1,z+1) :
            if g % i == 0 and g % j == 0 :
                jj = j
                
    else :
        g = y
        s = x
    
        
    
    
