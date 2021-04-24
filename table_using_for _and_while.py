a=int(input("Enter to number to print it's table: "))
print("Using for loop") 
for i in range(1,11):
    print(a," X ",i," = ",a*i)

print("Using while loop")   
#using while loop
i=1
while i<=10:
    print(a," X ",i," = ",a*i)
    i+=1
    continue
