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