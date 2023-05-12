##year=int(input("enter the year to be checked:"))
##if (year%400==0):
##    print(year,"is a leap year")
##elif(year%100==0):
##    print(year,"is not the leap year")
##elif(year%4==0):
##    print(year,"is the leap year")
##else:
##    print(year,"is not the leap")


##nested if

year=int(input("enter the year to be checked:"))
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print(year,"is leap year")
        else:
            print(year,"is not the leap year")
    else:
        print(year,"is leap year")
else:
    print(year,"is not the leap year")






