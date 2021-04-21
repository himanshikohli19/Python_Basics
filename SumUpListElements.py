list1=[]
sum1=0
num=int(input("Enter number of elements you want add: "))
for i in range(0,num):
    ele=int(input("Enter a number: "))
    list1.append(ele)

print("Sum of numbers in the list: ", sum(list1))
