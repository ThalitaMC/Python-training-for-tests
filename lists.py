
####Given a string containing letters and then a number, return an alphabetical list with the total sum of numbers corresponding to each letter
import os
s= "c2a2b7a6b2c5"
o1=[]
o2=[]
o3=[]
i=0
while i < len(s):
    if s[i] in o1:
        ind=o1.index(s[i])
        i=i+1
        o2[ind]= o2[ind] + int(s[i])
        print("i")
    else:
        print(i)
        o1.append(s[i])
        i=i+1
        print(i)
        o2.append(int(s[i]))
    i=i+1
i=0
while i < len(o1):
    o3.append(o1[i] + str(o2[i]))
    i=i+1
o3.sort()
print (s)
print (o1)
print (o2)
print (o3)


