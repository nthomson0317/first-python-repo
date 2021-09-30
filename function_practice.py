###########################################
#WARMUP#
################################

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
