### Methods
### functions that are built into objects

mylist = [1,2,3]

mylist.append(4)
#==> [1,2,3,4]

mylist.pop()
#==> 4
print(mylist)
#==> [1,2,3]

# help(mylist.insert)
#==> insert(index, object, /) method of builtins.list instance
    #==> Insert object before index.


### Functions

def name_of_function(name):
    '''
    Docstring explains function.
    '''
    print("Hello" + ', ' + name)

name_of_function('Jose')

#####

def add_function(num1, num2):
    return num1 + num2

result = add_function(1,2)
print(result)

####

def say_hello():
    print('hello')
    print('how')
    print('are')
    print('you?')

say_hello()

####

def say_hello(name='Default'):
    print(f'Hello, {name}')

say_hello('Nicholas')
say_hello()

def add_num(num1, num2):
    return num1 + num2

thirty = add_num(10,20)

print(thirty)
###

def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False