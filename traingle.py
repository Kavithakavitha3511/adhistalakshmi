a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if (a==b==c):
    print("equilateral triangle")
elif (a==b) or (b==c) or(c==a):
    print("isoscales triangle")
else:
    print("scale triangle")
