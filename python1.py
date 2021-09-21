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