#display prime number between 2 numbers
a=int(input())
b=int(input())
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if ((i%j)==0):
                break
        else:
            print(i)