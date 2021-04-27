#You just need to take string and a character as an input
#from stdin and print 'True' if that character is present in
#that string otherwise print 'False'.

a=input()
b=input()
boolean=False
for i in range(0,len(a)):
    if(a[i]==b):
        boolean=True
        break


if boolean==True:
    print(boolean)
else:
    print(boolean)
