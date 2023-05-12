tax=int(input("enter the tax price"))
if (tax>100000):
    x=((15/100)*100000)
    print("tax price:15%",x)
elif (tax>50000) and (tax<=100000):
    y=((10/100)*100000)
    print("tax price:10%",y)
elif (tax<=50000):
    z=((5/100)*50000)
    print("tax price:5%",z)
else:
    print("there is no tax")
