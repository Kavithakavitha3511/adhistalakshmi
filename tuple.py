highest and lowest

a=(1,4,3,5,7,8)
b=list(a)
print(b)
b[4]=32
print(b)
highest=b[0]
lowest=b[0]
for i in range(len(b)):
    if b[i]>highest:
        highest=b[i]
    else:
        lowset=b[i]
a=tuple(b)
print(a)
print(highest)
print(lowest)

ascending and descending order
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




