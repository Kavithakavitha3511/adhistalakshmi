a=(1,4,3,5,7,8)
b=list(a)
print(b)
b[4]=32
print(b)
a=tuple(b)
print(a)
highest=a[0]
lowest=a[0]
for i in range(len(a)):
    if a[i]>highest:
        highest=a[i]
    else:
        lowset=a[i]
print(highest)
print(lowest)


a=(4,3,5,7,8,1)
c=list(a)
print(c)
c[3]=15
print(c)
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]>c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)


a=(4,3,5,7,8,1)
c=list(a)
print(c)
c[3]=15
print(c)
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]<c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)




