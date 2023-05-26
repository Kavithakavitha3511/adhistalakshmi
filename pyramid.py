##rows=int(input("enter the rows"))
##for i in range(rows,0,-1):
##    for j in range(rows,i,-1):
##        print(end=" ")
##    for j in range(0,i):
##        print("*", end=" ")
##    print()
##for i in range(1,rows):
##    for j in range(0,rows-i-1):
##        print(end=" ")
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()


rows=int(input("enter the rows"))
for i in range(0,rows):
    for j in range(0,rows-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(rows,i,-1):
        print(end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print()

