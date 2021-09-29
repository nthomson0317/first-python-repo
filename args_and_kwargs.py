#### *args and **kwargs

def myfunc(a,b):
    #Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

result = myfunc(40,60)
print(result)

