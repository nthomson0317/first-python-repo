#### MAP
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

list(map(square,my_nums))


print('splicer')
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer,names)))

for name in map(splicer,names):
    print(name)


    ##### FILTER

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even,mynums):
    print(n)



##### LAMBDA

def square(num):
    result = num**2
    return result

square(3)
##==> 9

square = lambda num: num**2

square(5) 
#==> 25

print(list(map(lambda num:num**2,mynums)))
##==> [1, 4, 9, 16, 25, 36]

print(list(filter(lambda num:num%2==0, mynums)))
##==> [2, 4, 6]