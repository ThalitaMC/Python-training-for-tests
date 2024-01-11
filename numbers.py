#########Decimal to binary
'''
num=int(input("Enter an integer number: "))
print(bin(num)[2:])

bin_vec=[]
def binary(num):
    if num == 0 or num == 1 :
        bin_vec.append(num)
        return(bin_vec)
    else:
        bin_vec.append(num%2)
        return binary(int(num/2))
rev=binary(num)
print(rev)
print(rev[::-1])
'''
####Fibonatti
'''
a=0
b=1
limit=int(input("Enter the limit of numbers:"))-2
for i in range (limit):
    c=a+b
    a=b
    b=c
print(b)
'''
### Armstrong Number
'''
number1= input("Write a number to be verified:")
number2=0
factor = len(number1)
print (factor)
for i in range (factor):
    number2= number2 + int(number1[i]) ** factor
if number2 == int(number1):
    print("Armstrong!")
else:
    print("Not Armstrong!")
 ''' 
  ###Leap Year
def leapyear(ano):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = " is a Leap Year"
    else:
        result = " is not a Leap Year"
    return result
year = int(input("Type the year:"))
print(str(year) + str(leapyear(year)) )
