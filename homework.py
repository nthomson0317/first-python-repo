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