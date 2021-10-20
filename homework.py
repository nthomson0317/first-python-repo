## Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
  return  (4/3) * math.pi * (rad**3)

print(vol(2))


##Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high):
            print(f'{num} is in the range between {low} and {high}')
    else:
            print(f'{num} is NOT in the range between {low} and {high}')

ran_check(5,2,7)
ran_check(99,2,7)
ran_check(500,2,7000)
ran_check(15,2,7)
ran_check(55,2,70)

## Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    up = 0
    low = 0
    for i in s:
        if i.isupper():
            up +=1
        elif i.islower():
            low +=1
    print(f'No. of Upper case characters : {up}')
    print(f'No. of Lower case characters : {low}')



s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

## Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    new_list = set(lst)
    new_new_list = list(new_list)
    print(new_new_list)

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])