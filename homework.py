## Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
  return  (4/3) * (math.pi * (rad**3))

print(vol(2))
