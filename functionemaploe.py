#factorial funtion
def fac():
    stop=int(input("enter the stop value"))
    fac=1
    for i in range(1,stop+1):
        fac*=i
        print(fac)
    print("fac value:",fac)
fac()
fac()
fac()

##Swapping variables
def swap():
    a=10
    b=5
    a,b=b,a
    print("a is swapping", a)
    print("b ia swapping", b)
swap()

##even number
def even():
    stop=int(input("enter the stop value"))
    for i in range(1,stop+1):
        if(i%2==0):
            print(i)
even()
even()

odd number
def odd():
    stop=int(input("enter the stop value"))
    for i in range(1,stop+1):
        if(i%2!=0):
            print(i)
odd()
odd()

def sum():
    stop=int(input("enter the stop value"))
    num=0
    for i in range(1,stop):
        num=num+i
    print("total number of value:", num)
sum()




