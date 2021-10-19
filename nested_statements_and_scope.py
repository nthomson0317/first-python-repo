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

####

x = 50

def func(x):
    print(f'X is {x}')

    ## LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func(x)

y = 500
def function():
    global y
    print(f'Y is {y}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    y = 200
    print(f'I JUST LOCALLY CHANGED X TO {y}')

function()

