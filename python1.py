msg = ('hello world')
print(msg)

## reverse a string
print(msg[::-1])

print(20 % 2)

print(2 ** 3)

print('This is a string {}'.format('{a:b}'))

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))


##.format() method

result = 100/777

print("The result was {result}".format(result=result))
print ("The result was {r:1.3f}".format(r=result))


## string literal/ f strings/ formatted string literals

name = "jose"

print(f'Hello, his name is {name}')

name2 = "nicholas"
age = 31

print(f'{name2} is {age} years old')


####### Lists

my_list = [1,2,3]

my_list_2 = ['STRING', 100, 23.2]

print(len(my_list))

print(my_list[0])

print(my_list_2[1:])

list_3 = my_list + my_list_2

print(list_3)

list_3[0] = 'ONE ALL CAPS'

print(list_3)

##append adds item to end of list
list_3.append('six')
print(list_3)

##pop removes item from end of list

list_3.pop()

print(list_3)

popped_item = list_3.pop()

print(popped_item)

popped_index = list_3.pop(2)
print(popped_index)
print(list_3)


## sort

new_list = ['a', 'e', 'x', 'c', 'g']
num_list = [4,1,3,8,2]

new_list.sort()
num_list.sort()
print(new_list)
print(num_list)
my_sorted_list = new_list
## sort happens in place, so can't assign my_sorted_list to return value of new_list.sort() b/c that return value is None

##reverse

num_list.reverse()
print(num_list)

## Dictionaries

my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0,1,2], 'k3':{'insideKey': 100}}

print(d['k2'])

print(d['k3'])
print(d['k3']['insideKey'])

dic = {'key1': ['a','b','c']}
print(dic['key1'][2])
dic['key1'][2] = dic['key1'][2].upper()
print(dic)

dix = {'k1': 100, 'k2': 200, 'k3': 300}

dix['k4'] = 400

print(dix)

print(dix.keys)
print(dix.values)
print(dix.items())


## Tuples (immutable lists)
## tuples use parenthesis: (1,2,3)

t = (1,2,3)
mylist = [1,2,3]

type(t)
type(mylist)

t = ('one', 2)

print(t[0])
print(t[-1])
#[-1] indexes last item of the list

t = ('a', 'a', 'a')
count = t.count('a')
index = t.index('a')

print(count)
print(index)


## Sets (unordered collections of unique elements)

s = set()
s.add(1)
print(s)

s.add(2)
print(s)

s.add(2)
print(s)
## still just {1,2} won't duplicate values, 

mylist = [1,1,1,1,1,1,2,2,2,2,2,2]
setlist = set(mylist)
print(setlist)

## Booleans

True
False
b = None





s = 'hello'

## test

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])


######### Python comparison operators

2 == 2
#==>True

2 == 1
#==>False

'hello' == 'bye'
#==>False

'Bye' == 'bye'
#==>False

'2' == 2
#==>False

2.0 == 2
#==>True


##### Logical operators

1 < 2 < 3
#==> True

1 < 2 > 3
#==> False

1 < 2 and 2 > 3
#==> False

1 < 2 and 2 < 3
#==> True

'h' == 'h' and 2 == 2
#==> True

100 == 1 or 2 == 2
#==> True

not 1 == 1
#==>False


###Control flow syntax

if 3>2:
    print('ITS TRUE!')
#==> ITS TRUE!

hungry = True

if hungry:
    print('FEED ME!')
#==> FEED ME!

hungry = False

if hungry:
    print('FEED ME!')
else: print('Im not hungry')
#==> Im not hungry

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
else:
    print('I do not know much')
    #==> Money is cool!

## for loops

my_iterable = [1,2,3]
for i in my_iterable:
    print(i)



