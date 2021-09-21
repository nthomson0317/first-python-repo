msg = ('hello world')
print(msg)

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
print(new_list)

