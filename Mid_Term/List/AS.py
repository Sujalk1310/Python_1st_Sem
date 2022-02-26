k = str(input())
g = int(k[-1])
index = int(k)-1
list = []
for i in range (1,1001) :
    if i%3 != 0 and g != 3 :
        list.append(i)
print (list[index])
