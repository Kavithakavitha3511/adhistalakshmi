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

##EXAMPLE 
def swap():
    a=10
    b=6
    a,b=b,a
    print("a is swapping", a)
    print("b is swapping", b)
swap()

def swap(a,b):
    a,b=b,a
    print("a is swapping", a)
    print("b is swapping", b)
swap(10,6)


def swap(a,b):
    a,b=b,a
    print("a is swapping", a)
    print("b is swapping", b)
swap(a=20,b=10)


def swap(a,b=10):
    a,b=b,a
    print("a is swapping", a)
    print("b is swapping", b)
swap(60)

