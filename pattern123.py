rows=int(input("enter the row"))
cols=int(input("enter the cols"))
a=0
for i in range(1,rows+1):
    for j in range(1,cols+1):
        a+=1
        print(a, end=" ")
    print()
    
