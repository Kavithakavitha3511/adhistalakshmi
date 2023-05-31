num=int(input("enter the number"))
count=0
if num==1:
    print("it is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            count=1
            break
    if(count==1):
        print("it is a prime number")
    else:
        print("it is not a prime number")

***********************************************************

start_value=int(input("enter the start value"))
stop_value=int(input("enter the stop value"))
for i in range(start_value,stop_value+1):
    if i>1:
        count=0
        for j in range(2,i):
            if i%j==0:
                count=count+1
        if count==0:
            print(i)
            
*************************************************************    
start_value=int(input("enter the start value"))
stop_value=int(input("enter the stop value"))
for i in range(start_value,stop_value+1):
    if i>1:
        count=0
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i, end=" ")
