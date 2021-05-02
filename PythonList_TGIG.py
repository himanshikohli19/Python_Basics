#TechGIG Python List Problem
#Your task is to maintain a list and perform two types of queries on it : 
#Query '1' : It will be given as 1 x  : Insert x into the list.
#Query '2' : It will be given as 2 : Print the contents of the list.


n=int(input()) #to take the number of inputs
list1=[]
for i in range(n):
    f=[i for i in input().split()] #to accept multiple inputs at once
    a=f[0]  #to assign first entered value 1 or 2
    if (int(a)==2):
        print(list1)
    else: #case if entered 1 first
        b=f[1] 
        list1.append(b) 


