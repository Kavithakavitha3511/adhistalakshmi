#nested function
##def outer():
##    def inner():
##        return "i am inner function"
##    return inner()
##print(outer())

def func1(func):
    print("Hi i am func1 call func2")
    func()
def func2():
    print("hi am func2")
print(func2)
func1(func2)
