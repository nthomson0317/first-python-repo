x = 25

def printer():
    x = 50
    return x


print(x)
#==> 25

print(printer())
#==> 50

##Local

lambda num:num**2

##Enclosing

name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'
    def hello():
        print('Hello ' +name)
    hello()
greet()

