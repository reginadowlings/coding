import random
comp_guess = random.randint(1,9)

# user_guess = input('Guess the number')

# # while user_guess != comp_guess:
# #     user_guess = input('Guess the number')

# def random_number():
#     if int(user_guess) == comp_guess:
#         return 'That is a great guess!'

#     else:
#         return ''

# print(random_number())
# print(comp_guess)


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

# number =  int(input('What is your favorite number: '))

# if (number % 2) == 0:
#     print('That is even')
# else:
#     print('that is odd')
'''
total = 0
for num in range(101):
    total = total + num
    print(total)'''

'''print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
# '''
# import sys                                    
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')


# This is a guess the number game.

'''import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

 # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))'''

# Write a function, positive_numbers, that takes a list of numbers as its parameter.
# The positive_numbers function should return a list containing those of the numbers that are strictly greater than 0.

'''def positive_numbers(numbers):
    items = []
    for n in numbers:
        if n > 0:
            items.append(n)
    return items
'''
#  In other words, you should combine these colors with one another in all possible ways, except that the combined colors should 
# not be the same. Print each color combination.

'''colors = ["red", "green", "blue"]'''

# your code goes here
'''for color1 in colors:
    for color2 in colors:
        if color1 == color2:
            continue
        print(color1, '-', color2)'''


# Write a function named unique that takes a single parameter. The function will be called with a string as its argument.
# Your function should return a new string containing all the unique letters of the input string
'''
def unique(characters):
    special_characters = ''
    for c in characters:
        if c not in special_characters:
            special_characters += c
    return special_characters'''



# Write a function, initials, that takes one string as a parameter.The initials function should return a new string containing
# only those of the letters of the input string that are uppercase.

'''def initials(name):
    upper_case = ''
    for n in name:
        if n.isupper():
            upper_case +=n
    return upper_case

print(initials('Regina Dowlings'))'''

# my_list = [1, 2, 3, 0, 4, 5]
# sum_of_elements = 0

# for num in my_list:
#     if num == 0:
#         break
#     sum_of_elements += num

# print(sum_of_elements)

'''
import datetime
def addDays( year , month , day , dayincrement ):
    startdate = datetime.datetime( year , month , day )
    enddate = startdate + datetime.timedelta( days=dayincrement )
    return enddate.year , enddate.month , enddate.day
y, m, d = addDays( 2015, 11, 13, 55 )
print( "{}/{}/{}".format( y, m, d ) )'''

# apple = "apple"
# banana = "banana"
# cherry = "cherry"
# durian = "durian"

# def printfruits_1 ():
#     print( apple , banana )

# def printfruits_2( apple ):
#     banana = cherry
#     print( apple , banana )

# def printfruits_3( apple , banana ):
#     cherry = "mango"
#     banana = cherry
#     print( apple , banana )
 
# printfruits_1 ()
# printfruits_2( cherry )
# printfruits_3( cherry , durian )


# print( "apple =", apple )
# print( "banana =", banana )
# print( "cherry =", cherry )
# print( "durian =", durian )


# Write a function named equal_coordinates that takes as input a list of coordinates. Each coordinate is represented as a tuple 
# of numbers (x, y). Your function must return a list containing all those coordinates where x == y.
'''
def equal_coordinates(coordinates):
    same_coords = []
    for x, y in coordinates:
        if x == y:
            same_coords.append((x,y))
    return same_coords'''



# Write a function named trim that takes two parameters. The first parameter is a string s. The second parameter is a tuple of 
# numbers (begin, end). The trim function should return the part of s that starts at index begin and ends at index end.

'''def trim(string, numbers):
    x, y = numbers
    result = string [x:y] 
    return result'''

'''ages = {
    "Alice": 25,
    "Bob": 30,
    "Eve": 42,
    "Camilla": 23
}
print(ages["Camilla"])'''

'''
colors = {
    "sky": "blue",
    "stone": "grey",
    "wood": "brown",
    "sun": "yellow",
    "cloud": "white"
}

for value in colors.values():
    print(value)
'''

# for numbers in range (11):
#     numbers.reverse()
#     print(numbers)

# name = 'Tennessee'
# print(name.count('e'))


# Ask the user to enter three numbers. Then print the largest, the smallest,and their average, rounded to 2 decimals.

# x, y, z = map(int, input('Enter three numbers: ').split())
# highest = max(x,y,z) 
# print(round(highest, 2))

# lowest = min(x,y,z)
# print(round (lowest, 2))

# average =( x + y +z )/ 3
# print(round(average, 2))


# Write the function isOdd(), which determines whether a number is odd, by calling the function isEven() and inverting its result.

def isEven(number):
    return number % 2 == 0

def isOdd(number):
    return not isEven(number)


print(isEven(24))


print('happy')





















