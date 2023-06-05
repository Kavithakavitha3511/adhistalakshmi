##capitalize

txt="hello, and welcome to my world."
x=txt.capitalize()
print(x)

##casefold

txt="Helloo, and welcome to my world"
x=txt.casefold()
print(x)


##center

txt="banana"
x=txt.center(50)
print(x)

##count

txt=" I love apples, apple are my favorite"
x=txt.count("apple")
print(x)

##endswith

txt="Hello, and welcome to my world."
x=txt.endswith("my world.")
print(x)


##expandtabs

txt="H\te\tl\tl\to"
print(txt.expandtabs(4))

find()

txt="Hello, welcome to my world."
x=txt.find("my")
print(x)

##format

txt="for only {price:.2} dollars!"
print(txt.format(price=49))


##index

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

##isalnum

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)


##isalpha
txt = "Company10"
x = txt.isalpha()
print(x)

txt = "Company"
x = txt.isalpha()
print(x)


##ascci
txt = "Company123"
x = txt.isascii()
print(x)


##isdecimal

txt = "1234"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

##isidentifier
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

##islower

txt = "hello world!"
x = txt.islower()
print(x)

##numeric

txt = "565543"
x = txt.isnumeric()
print(x)












