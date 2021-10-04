###########################################
#WARMUP#
###########################################

#WRITE A FUNCTION THAT RETURNS THE LESSER OF TWO GIVEN NUMBERS IF BOTH NUMBERS ARE EVEN, BUT RETURNS THE GREATER IF ONE OR BOTH NUMBERS ARE ODD

def lesser_of_two_evens(a,b):
    if (a % 2 == 0) and (b % 2 == 0):
        if (a > b):
            return b
        else:
            return a
    elif (a % 2 != 0) or (b % 2 != 0):
        if (a > b):
            return a
        else:
            return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))


#WRITE A FUNCTION THAT TAKES A TWO-WORD STRING AND RETURNS TRUE IF BOTH WORDS BEGIN WITH THE SAME LETTER

def animal_crackers(str):
    words = str.split(' ')
    if words[0][0] == words[1][0]:
        return True
    else: 
        return False
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#GIVEN TWO INTEGERS, RETURN TRUE IF THE SUM OF HTE INTEGERS IS 20 OR IF ONE OF THE INTEGERS IS 20. IF NOT, RETURN FALSE

def makes_twenty(a,b):
    if (a == 20) or (b == 20):
        return True
    elif (a + b == 20):
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))


###########################################
#LEVEL 1#
###########################################

#### WRITE A FUNCTION THAT CAPITALIZES THE FIRST AND FOURTH LETTERS OF A NAME

def old_macdonald(name):
    new_str = ''
    for i in range(len(name)):
        if i == 0:
            new_str += (name[i].upper())
        elif i == 3:
            new_str += (name[i].upper())
        else: 
            new_str += (name[i])
    return new_str

print(old_macdonald('macdonald'))


#### GIVEN A SENTENCE, RETURN A SENTENCE WITH THE WORDS REVERSED

def master_yoda(sentence):
    split = sentence.split(' ')
    split.reverse()
    new_str = ' '.join(split)
    return new_str

print(master_yoda('I am home'))

print(master_yoda('We are ready'))

### ALMOST THERE: GIVEN AN INTEGER, N, RETURN TRUE IF IN IS WITHIN 10 OF EITHER 100 OR 200

def almost_there(n):
 if n in range(90, 110) or n in range(190,210):
     return True
 else: 
     return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

###########################################
#LEVEL 2#
###########################################

####FIND 33: GIVEN A LIST OF INTS, RETURN TRUE IF THE ARRAY CONTAINS A 3 NEXT TO A 3 SOMEWHERE

def has_33(nums):
    for i in range(0, len(nums)-1):
    #  if nums[i] == 3 and nums[i] == nums[i+1]:
        if nums[i:i+2] == [3,3]:
            return True

    return False


print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

#### PAPER DOLL: GIVEN A STRING, RETURN A STRING WHERE FOR EVERY CHARACTER IN THE ORIGINAL THERE ARE THREE CHARACTERS

def paper_doll(text):
    new_str = ''
    for i in text:
        new_str += (i*3)
    return new_str

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

#### BLACKJACK: GIVEN THREE INTEGERS BETWEEN 1 AND 11, IF THEIR SUM IS LESS THAN OR EQUAL TO 21, RETURN THEIR SUM. IF THEIR SUM EXCEEDS 21 AND THERE'S AN 11, REDUCE THE TOTAL SUM BY 10. FINALLY, IF HTE SUM (EVEN AFTER ADJUSTMENT) EXCEEDS 21, RETURN 'BUST'

def blackjack(a,b,c):
    if (a + b + c) <= 21:
        return (a + b + c)
    elif (a + b + c) > 21 and (a == 11 or b == 11 or c == 11):
        return ((a + b + c) - 10)
    else:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#### SUMMER OF '69: RETURN THE SUM OF THE NUMBERS IN THE ARRAY, EXCEPT IGNORE SECTIONS OF NUMBERS STARTING WITH A 6 AND EXTENDING TO THE NEXT 9(EVERY 6 WILL BE FOLLOWED BY AT LEAST ONE 9). RETURN 0 FOR NO NUMBERS

def summer_69(arr):
    sum = 0
    add = True
    for n in arr:
        while add:
            if n != 6:
                sum += n
                break
            else:
                add = False
        while not add:
            if n != 9:
                break
            else:
                add = True
                break
        return sum
        
        


print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))

#### SPY GAME: WRITE A FUNCTION THAT TAKES IN A LIST OF INTEGERS AND RETURNS TRUE IF IT CONTAINS 007 IN ORDER

def spy_game(nums):
    pass

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))