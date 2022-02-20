s1 = input()
s2 = input()
x = ''
for i in s1:
    if i not in s2 :
        x += i
for j in s2 :
    if j not in s1 :
        x += j
st = ''
for i in x :
    if i not in st :
        st += i
print (st)
