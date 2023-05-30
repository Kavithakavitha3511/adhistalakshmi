   *
  * *
* * * *


num=int(input("enter the no of rows"))
row=0
while row<num:
    a=num-row-1
    while a>0:
        print(end=" ")
        a=a-1
    b=row+1
    while b>0:
        print("*",end=" ")
        b=b-1
    row=row+1
    print()
        
        


*****
****
***
**
*


num=int(input("enter the no of rows"))
i=1
while i<=num:
    j=num
    while j>=i:
        print("*", end=" ")
        j=j-1
    print()
    i=i+1


*
**
***
****
*****
num=int(input("enter the no of rows"))
i=0
while(i<=num):
    print("*", end=" ")
    j=1
    while(j<=i):
        print("*", end=" ")
        j=j+1
    print()
    i=i+1


*
**
***
****
*****
****
***
**
*

num=int(input("enter the no of rows"))
i=0
while(i<=num):
    print("*", end=" ")
    j=1
    while(j<=i):
        print("*", end=" ")
        j=j+1
    print()
    i=i+1
i=1
while i<=num:
    j=num
    while j>=i:
        print("*", end=" ")
        j=j-1
    print()
    i=i+1

