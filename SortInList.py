print("WELCOME STUDENTS!")
list_marks=[]
for i in range(0,6):
    marks=int(input("Enter marks of student: "))
    list_marks.append(marks)
list_marks.sort(reverse=False)
print("These are the marks of students in sorted order:\n", list_marks)
