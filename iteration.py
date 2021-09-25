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


mylist = [(1,2),(3,4),(5,6),(7,9)]
len(mylist)
#==> 4

for i in mylist:
    print(i)

for (a,b) in mylist:
    print(a)
    print(b)