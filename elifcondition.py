###4. no of days 1 to 7:
##day=int(input("enter the no of days 1-7"))
##if(day==1):
##    print("sunday",day)
##elif(day==2):
##    print("monday",day)
##elif(day==3):
##    print("tuesday",day)
##elif(day==4):
##    print("wednesday",day)
##elif(day==5):
##    print("thursday",day)
##elif(day==6):
##    print("friday",day)
##elif(day==7):
##    print("saturday",day)
##else:
##    print("day is not defined")




unit=int(input("enter the units"))
if(unit<=100):
    print("no charge")
elif(unit<=200):
    a=((unit-100)*5)
    print("next 100 units price",a)
elif(unit>200):
    b=((unit-200)*10)+500
    print("after 200 unit",b)
    
