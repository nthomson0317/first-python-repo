#### *args and **kwargs

def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05

result = myfunc(40,60,100,100,3)
print(result)
#==>15.15

################################################################

def myfunctwo(*args):
    #Returns 5% of the sum of a and b
    return sum((args)) * 0.05

result = myfunctwo(1,2,3,4,5,6,100,200,300,400,500,978)
print(result)
#==>124.95
