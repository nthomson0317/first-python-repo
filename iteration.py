mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    print('hello')


for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)
#==> 55

mystring = 'Hello World'

for letter in mystring:
    print(letter)


tup = (1,2,3)

for i in tup:
    print(i)

##tuple iteration

mylist = [(1,2),(3,4),(5,6),(7,9)]
len(mylist)
#==> 4

for i in mylist:
    print(i)

##tuple unpacking
for (a,b) in mylist:
    print(a)
    print(b)

newlist = [(1,2,3),(4,5,6),(7,8,9)]

for (a,b,c) in newlist:
    print(b)
    #==> 2 6 9


##dictionary

d = {'k1': 1, 'k2': 2, 'k3': 3}

for i in d.items():
    print(i)
#==>('k1', 1)
#==>('k2', 2)
#==>('k3', 3)

for key,value in d.items():
    print(value)
    #==> 1
    #==> 2
    #==> 3


######### while loops (execute a block of code while some condition remains true)

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1