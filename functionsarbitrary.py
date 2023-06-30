#Default parameter
def function_name(name="Kalai"):
    print(name)
function_name("Priya")
function_name("Swetha")
function_name()

#Arbitrary
def function_name(**kid):
    print("Last name is "+kid["lname"])
function_name(fname="Kalai", lname="Swetha")


#Passing list to argument
def function_name(food):
    for x in food:
        print(x)
food_name=["idly","dosa","rice"]
function_name(food_name)

#return value
def function_name(x):
    return(5*x)
print(function_name(6))
print(function_name(2))
print(function_name(8))
print(function_name(7))

for i in range(0,6):
    pass
    
    

    
