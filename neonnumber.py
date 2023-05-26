##neon number=9
##9*9=81
##8+1=9

number=int(input("enter the number")) 
sum=0
sqr=number*number
print("square of the given number:",sqr)
while(sqr>0):
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
print("sum of the given number:",sum)
if(sum==number):
    print("number is neon")
else:
    print("number is not a neon number")


##neven number
##21=>2+1
##
##21/2+1=7

number=int(input("enter the number"))
a=number
sum=0
rem=0
while(a>0):
    rem=a%10
    sum=sum+rem
    a=a//10
print("sum of the given number",sum)
if (number%sum==0):
    print(number,"is a niven number")
else:
    print(number,"is not a niven number")



factors of number
5
5 is divided by (1,3,5)






    
