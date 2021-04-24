#check whether a number is prime or not
a=int(input("Enter a number: "))
for i in range(2, a):
    if (a%i==0):
        prime=False
    else:
        prime=True

if prime == True:
    print("the number in Prime")
else:
    print("The number in Composite")
