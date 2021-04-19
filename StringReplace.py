import datetime
str1='''Dear NAME,

Congratulations, You got selected!

Thank you!
Undersigned
DATE
'''
name = input("Enter your name: ")
d = str(datetime.datetime.now())
str1=str1.replace("NAME", name)
str1=str1.replace("DATE", d)
print(str1)
