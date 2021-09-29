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
    return False #on the indent level of the for loop NOT the if statement

listone = [1,3,5,17,23,435,223,4]

print(check_even_list(listone))

def collect_even_list(list):
    even_numbers = []

    for i in list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

listy = [0,2,5,3,2,424,66,54,222,41,52,34,5,2,1,3]

res = collect_even_list(listy)
print(res)

#### tuple unpacking

stock_prices = [('APPL', 200),('GOOG', 400),('MSFT', 100)]

for item in stock_prices:
    print(item)
#==>('APPL', 200)
#==>('GOOG', 400)
#==>('MSFT', 100)

for ticker,price in stock_prices:
    print(ticker)
#==>APPL
#==>GOOG
#==>MSFT

for ticker,price in stock_prices:
    print(price+(0.1*price))
#==> 220.0
#==> 440.0
#==> 110.0

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return(employee_of_month,current_max)

result = employee_check(work_hours)
print(result)
#==> ('Cassie', 800)
name,hours = employee_check(work_hours)
print(name)
#==> Cassie
print(hours)
#==> 800

#### interactions between functions

example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)
print(example)