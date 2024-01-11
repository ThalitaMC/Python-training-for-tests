##############-----------------------##############
####Given a string containing letters and then a number, return an alphabetical list with the total sum of numbers corresponding to each letter
'''
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
'''
##############-----------------------##############
###Reverse numbers:
'''
input
n=1234
n=str(n)
n2=0
size=len(n)
for i in range (size):
    n2=n2+int(n[i])*(10**(i))
print(n2)
''' 
##############-----------------------##############
 ##Palindrome: Is the input a palindrome?
'''
string = input("Write a string:")
size=len(string)
palindrome = True
for i in range (int(size/2)):
    print(i, size)
    if string[i] != string[size-i-1]:
        palindrome = False
print(palindrome)
'''
##############-----------------------##############
##Find the missing number in a given array
##Given an array of positive numbers ranging from 1 to n, such that all numbers from 1 to n are present except one number x,
# find x. Assume the input array is unsorted.
'''
import random

#Creating the array
def createarr():
    n = int(input("n:"))
    missing = random.randint(1,n)
    num_list = list(range(1, n+1))
    num_list.pop(missing)
    random.shuffle(num_list)
    print(num_list)
    return(num_list,n)

#With a given array:
def givenarr():
    num_list = [5, 3, 1, 7, 2, 8, 4, 6]
    n= len(num_list) + 1
    return(num_list,n)
#
num_list,n = givenarr() # createarr() # 
for i in range(1, n+1):
    if i not in num_list:
        print("x is: ", i)
'''
##############-----------------------##############
##Determine if the sum of two integers is equal to a given value
##Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
# Return true if the sum exists, and false if it does not. Consider the following array and its target sums:
'''
def checksum(target):
    check = False
    numlist = [5,7,1,2,8,4,3]
    for i in range(0,len(numlist)):
        for j in range(i+1, len(numlist)):
            if target == numlist[i]+numlist[j]:
                check = True
                print(target, "=", numlist[i], "+", numlist[j])
    if check == False:
        print("No two values sum up to", target)

checksum(10)
checksum(19)
'''
##############-----------------------##############