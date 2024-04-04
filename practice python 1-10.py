
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year
#  that they will turn 100 years old. 

user_name = input('What is you name: ')
user_age = int(input('What is your age: '))
turning_100 = 100 - user_age

year_when_turned_cen_old = 2023 + turning_100

print(user_name, 'you will trun 100 in the year', year_when_turned_cen_old )

#  Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

num = int(input('give me a number: '))

if num % 2 ==0:
    print('You entered an even number')
else:
    print('That is odd!')


# write a program that prints out all the elements of the list that are less than 5.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in numbers:
    if num < 5:
        print(num)


# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know
#  what a divisor is, it is a number that divides evenly into another number. 

user_number = int(input('What\'s your favorite number: '))

divisors = []
for i in range(1, user_number+1):
    if user_number % i == 0:
        divisors.append(i)
# print('The divisors of', user_number, 'are', divisors)


# write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


def common_numbers(list1, list2): 
    result = []

    set_1 = set(list1) 
    set_2 = set(list2)

    for ele in set_1:
        for num in set_2:
            if ele == num:
                result.append(ele)
    return result

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

same = common_numbers(a, b)
print(same)


# write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your 
# program works on two lists of different sizes. Write this in one line of Python 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
same = set([element for element in a if element in b])
print(list(same))


# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards 
# and backwards.)

string = input('give me a word: ')
string_backwards = string[:: -1]

if string == string_backwards:
    print('The word', string, 'is a palindrome ')
else:
    print('Your word', string, 'isn\'t a palindrome')


# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to
#  the winner, and ask if the players want to start a new game)
import random 

def rps_game():

    choices = ['rock','paper', 'scissors']

    user_input = input('Choose on of the choice: ')

    computer_guess = random.choice(choices)
    print('Computer played', computer_guess)

    if user_input == computer_guess:
        print('it is a tie')

    elif user_input == 'rock':
        if computer_guess == 'paper':
            print('computer win')
        else:
            print('you win')

    elif user_input == 'paper':
        if computer_guess == 'scissors':
            print('computer wins')
        else:
            print('you win')

    elif user_input == 'scissors':
        if computer_guess == 'rock':
            print('computer wins')
        else:
            print('you win')
    
    else:
        print('You didn\'t enter a valid choice')

rps_game()


# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. 
import random

random_guess = random.randint(1,9)

user_guess = int(input('Guess a number between 1 and 9: '))


if user_guess == random_guess:
    print('You guessed right!')
elif user_guess < random_guess:
    print('your guess is too low')
elif user_guess > random_guess:
    print('your guess is too high')
else:
    print('no correct input entered')







