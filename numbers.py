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
a=0
b=1
limit=int(input("Enter the limit of numbers:"))-2
for i in range (limit):
    c=a+b
    a=b
    b=c
print(b)
