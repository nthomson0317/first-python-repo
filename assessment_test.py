#1. 

sentence = 'Print only the words that start with s in this sentence'

split_sentence = sentence.split(' ')

for word in split_sentence:
    if word[0] == 's': print(word)

#2. Use range() to print all the even numbers from 0 to 100

for num in range(0,101):
    if num % 2 == 0:
        print(num)
#3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

list = [x for x in range(0,51) if x % 3 == 0]
print(list)

#4. Print all words in string whose length is even

st = 'Print every word in this sentence that has an even number of letters'

split = st.split(' ')

for word in split:
    if len(word) % 2 == 0:
        print(word)

#5. FizzBuzz

for num in range(0,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz')
    elif (num % 3 == 0):
        print('Fizz')
    elif (num % 5 == 0):
        print('Buzz')
    else: print(num)