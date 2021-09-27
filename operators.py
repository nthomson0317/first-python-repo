#### RANGE ####

mylist = [1,2,3]

for num in range(10):
    print(num)
#==> prints 0 through 9

for num in range(3,10):
    print(num)
#==> prints 3 through 9

for num in range(0,10,2):
    print(num)
    #==> prints 0 2 4 6 8

list(range(0,11,2))
#==>[0, 2, 4, 6, 8, 10]

#### ENUMERATE ####

##v1
index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count +=1
##v2
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count +=1

##v3

word = 'abcde'

for item in enumerate(word):
    print(item)
#==>(0, 'a')
#==>(1, 'b')
#==>(2, 'c')
#==>(3, 'd')
#==>(4, 'e')
#enumerate prints tuples!


#### ZIP ####

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)
#==> (0, 'a')
#==>(1, 'b')
#==>(2, 'c')
#==>(3, 'd')
#==>(4, 'e')

list(zip(mylist1, mylist2))
#==>[(1, 'a'), (2, 'b'), (3, 'c')]

#### IN ####

'x' in [1,2,3]
#==> False

'x' in ['x','y','z']
#==> True

'a' in 'a world'
#==> True

'mykey' in {'mykey': 345}
#==> True

d = {'mykey':345}
345 in d.values()
#==> True

d = {'mykey':345}
345 in d.keys()
#==> False

#### MIN MAX ####
mylist = [10,20,30,40,100]
min(mylist)
#==> 10

max(mylist)
#==> 100

#### RANDOM ####

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
#==> [1, 9, 10, 7, 2, 8, 4, 6, 5, 3]

from random import randint

randint(0,100)
#==> random integer

#### ACCEPT USER INPUT ####

result = input('Enter a number here: ')
## 50
print(result)

##=> 50

type(result)
#==> string

float(result)
#==> 50.0
int(result)
#==> 50

type(result)
#==> int

### list comprehensions

mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
    #=> ['h','e','l','l','o']

mylist = [letter for letter in mystring]
print(mylist)
 #=> ['h','e','l','l','o']

mylist2 = [x for x in 'word']
print(mylist2)

mylist = [num for num in range(0,11)]
print(mylist)
#==>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [num**2 for num in range(0,11)]
print(mylist)
#==>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = [x for x in range(0,11) if x%2 == 0]
print(mylist)
#==> [0, 2, 4, 6, 8, 10]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)* temp + 32) for temp in celcius]
print(fahrenheit)
#==>[32.0, 50.0, 68.0, 94.1]

fahrenheight = []

for temp in celcius:
    fahrenheit.append(( (9/5)* temp + 32))
#==>[32.0, 50.0, 68.0, 94.1]

results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)
#==>[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)
#==>[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)
#==>[2, 20, 2000, 4, 40, 4000, 6, 60, 6000]