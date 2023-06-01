name=(input("enter the name"))
print("hello"+" "+name+"!")         ##hello_name('Bob') → 'Hello Bob!'


a=(input("enter a:"))
b=(input("enter b:"))
print(a+b+b+a)                       ####make_abba('Hi', 'Bye') → 'HiByeByeHi'


a=(input("enter a:"))
b=(input("enter b:"))
print("<"+a+">"+b+"<"+"/"+a+">")     ##make_tags('i', 'Yay') → '<i>Yay</i>' 
  


a=(input("enter a:"))
b=(input("enter b:"))
print(a[0:2]+b+a[2:4])            ##make_out_word('<<>>', 'Yay') → '<<Yay>>'                           


a=(input("enter a:"))
print(a[-2:]+a[-2:]+a[-2:])           ####extra_end('Hello') → 'lololo'
                          

a=(input("enter a:"))
print(a[0:2])                     ####first_two('Hello') → 'He'               


a=(input("enter a:"))
b=(input("enter b:"))
print(b+a+b)                    ####combo_string('Hello', 'hi') → 'hiHellohi'            


a=(input("enter a:"))
b=(input("enter b:"))
print(a[1:]+b[1:])              ####non_start('Hello', 'There') → 'ellohere'


a=(input("enter a:"))
print(a[2:]+a[0:2])           #### left2('Hello') → 'lloHe'

 
a=(input("enter a:"))
b=len(a)//2
print(a[0:b])            ####first_half('WooHoo') → 'Woo'


a=(input("enter a:"))
print(a[1:-1])          ####without_end('Hello') → 'ell'



