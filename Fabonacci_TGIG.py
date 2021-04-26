#You just need to take a number as input from
#stdin which will tell how many terms of the Fibonacci needs to be printed.
#FABONACCI
num=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,num-2):
    sum1=a+b
    print(sum1,end=" ")
    a=b
    b=sum1


