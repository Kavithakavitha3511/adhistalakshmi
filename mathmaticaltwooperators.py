num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
operator=input("enter the operator")
if operator=="+":
    addition=num1+num2
    print("addition",addition)
elif operator=="-":
    sub=num1-num2
    print("sub",sub)
elif operator=="*":
    multiplication=num1*num2
    print("multiplication",multiplication)
elif operator=="/":
    division=num1/num2
    print("division",division)
else:
    print("enter the correct value of num1 and num2")
