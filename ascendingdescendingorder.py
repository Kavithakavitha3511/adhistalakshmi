#minimum and maximum ascending and descending
a=[1,4,3,56,32]
a.sort()
print("ascending order",a)
a.reverse()
print("Descending order",a)
print(max(a))
print(min(a))

#minimum and maximum
a=[1,4,3,5,7,8]
highest=a[0]
lowset=a[0]
for i in range(len(a)):
    if a[i]>a[0]:
        highest=a[i]
    else:
        lowest=a[i]
print(highest)
print(lowest)

#ascending and descending order
a=[4,3,5,7,8,1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]<a[j]):
            a[i],a[j]=a[j],a[i]
print(a)


#append
a=[]
length=int(input("enter the length list"))
for i in range(length):
    b=int(input("enter the value"))
    a.append(b)
print(a)
