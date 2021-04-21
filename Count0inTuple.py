#counting zeroes in a tuple
tuple1=(1,3,0,6,6,0,3,8,0,3,0,5,9)

#using count()
print("Number of zeroes occured in the tuple: ",tuple1.count(0))

#without using count function
count=0
for i in range(0,len(tuple1)):
    if tuple1[i]==0:
        count+=1
    else:
        continue

print("Number of zeroes occured in the tuple: ",count)
