n=int(input("Enter the number of elements: "))
a=[]
for j in range(0,n):
    ele=int(input("Enter the element: "))
    a.append(ele)
    
g=a[0]
for i in range(0,len(a),1):
    if a[i]>g:
        g=a[i]
    else:
        continue

print("Greatest number: ", g)
