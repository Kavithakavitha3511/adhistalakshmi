#argument
def add():
    a=5
    b=2
    print(a+b)
add()

def add(a,b):
    print(a+b)
add(5,6)

#keyword argument
def add(a,b):
    print(a+b)
add(b=5,a=6)

#default value 
def add(a,b=6):
    print(a+b)
add(8)
    
