## Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
  return  (4/3) * math.pi * (rad**3)

print(vol(2))


##Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high):
            return True
    else:
            return False

print(ran_check(5,2,7))
print(ran_check(99,2,7))
print(ran_check(500,2,7000))
print(ran_check(15,2,7))
print(ran_check(55,2,70))