a=int(input("Enter marks of subject 1: "))
b=int(input("Enter marks of subject 2: "))
c=int(input("Enter marks of subject 3: "))

if (((a/100)*100)>33) and (((b/100)*100)>33) and (((c/100)*100)>33) and (((a+b+c)/100)*100):
    print("You have passed the exam with flying colors!!")
else:
    print("Unfortunately, you've failed the test!")
