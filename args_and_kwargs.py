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

################################################################

def myfunc(*args):
    for item in args:
        print(item)
myfunc(40,60,200,100,300)
#==> 40
#==> 60
#==> 200
#==> 100
#==> 300

################################################################
################################################################

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple')
#==>My fruit of choice is apple

myfunc(fruit='apple',veggie='lettuce')
#==>My fruit of choice is apple

#################################

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dogs')
