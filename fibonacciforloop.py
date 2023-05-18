#fibonacci series
stop=int(input("enter the stop value"))
a=0
b=1
print(a, end=" ")
print(b, end=" ")
for i in range(1,stop):
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    c=a
    
##    
##fisrt+second
##0           =0
##1           =1
##0+1         =1
##1+1         =2
##1+2         =3
##2+3         =5
##3+5         =8
##5+8         =13
##8+13        =21
##13+21       =34
##21+34       =55    

