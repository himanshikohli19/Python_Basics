#First line will contain an Integer N,
#denoting  the number of students in the class.
#Each of the Next N lines will contain a string S denoting the student name,
#followed by five integers m1, m2, m3, m4, m5 denoting the marks scored
#in each subject.

#Input
#2
#arpit 100 75 40 56 53
#anushka 100 100 76 100 100

#Output
#100.00 87.50 58.00 78.00 76.50

N=int(input())
L=[]
for i in range(N):
    new_list = input()
    new_list = new_list.split()
    del new_list[0]
    new_list = [int(i) for i in new_list]
    L.append(new_list) #split to convert string into list with

res = [((sum(j)/(100*N))*100) for j in zip(*L)]

for i in res:
    print(("{0:.2f}".format(i)),end=" ")

