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
print(is_even(20))
print(is_even(21))

def even_check(number):
    return number % 2 == 0

####
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def check_even_list(list):
    for i in list:
        if i % 2 == 0:
            return True
    return False #on the level of for loop NOT if statement

listone = [1,3,5,17,23,435,223,4]

print(check_even_list(listone))