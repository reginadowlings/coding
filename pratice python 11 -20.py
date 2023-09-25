# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no 
# divisors.).

'''def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")'''


# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of
# the given list. For practice, write this code inside a function.

# def bend(numbers):
#     if not numbers:
#         return []
#     return [numbers[0], numbers[-1]]

# a = [5, 10, 15, 20, 25]
# first_last = bend(a)
# print(list(first_last))

'''RETURNING THE FIRST INDEX'''

def first_number(numbers):
    for num in numbers:
        return [numbers[0]]

numbers= [3, 5, 9, 11, 23]
first = first_number(numbers)
print(first)


# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you 
# can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
# def fibonnaci(numbers):

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# USING SETS

def numbers(list_of_nu):
    new_list = list(set(list_of_nu))
    # without_duplis= set(list_of_nu)
    return new_list

ages = [1,4,5,2,1,4,6,4,9]
new_age_list = numbers(ages)
print(new_age_list)


# USING FOR LOOP
'''
def get_unduplicated_list(list_of_numbers):
    new_list = []
    for num in list_of_numbers:
        if num in new_list:
            continue
        new_list.append(num)
    return new_list
    
ages = [1,4,5,2,1,4,6,4,9]
new_age_list = get_unduplicated_list(ages)
print(new_age_list)'''


# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, 
# except with the words in backwards order. 
    
# def reverse_string(multiple_strings):
#     splitting = multiple_strings.split()
#     reversed_strings = ''.join(reversed(splitting))
#     return  reversed_strings

# input_strings = input('Make a sentence of 5 words: ')
# reversing = reverse_string(input_strings)
# print(reversing)


# name = 'regina'
# rev = name[::-1]
# print(rev)


# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.


# import random
# characters = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm!@#$%^*'

# while True:
#     user_prompt = input("Enter 'generate' to get password or 'exit' to quit: ")
#     if user_prompt == 'exit':
#         break
#     elif user_prompt == 'generate':
#         length = random.randint(10,15)
#         password = ''.join(random.choices(characters,  k = length))
#         print(password)
#     else:
#         print('No prompt entered')



# name = input('enter your name: ')

# while True:
#     if name == '':
#         print('you did not enter your name')
#         name = input('enter your name: ')
#     else:
#         print(f'annyeong, {name}')
#         break

# import random
# import string 
# length = random.randint(9,12)

# ran_charaters = ''.join(random.choices(string.ascii_letters,  k = length))
# print(ran_charaters)


# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# number = []

'''def list_of_strings(list, number):
    ordered_list = sorted(list)
    if number in ordered_list:
        return True
    else:
        return False

nums = [2,3,6,5,1,4]
order = list_of_strings(nums, 7)
print(order)
    '''  

# a = '---'.join('    ')
# b = '   '.join('||||')
# print('\n'.join((a, b, a, b, a, b, a)))


# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)


# You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too 
# high, too low, or your number. At the end of this exchange, your program should print out how many guesses it took to get your number.
import random


program_guess = random.randint(0,100)

num_of_guesses = 1

while True:
    user_number= int(input('Guess a number between 0 and 100: '))
    if program_guess == user_number:
        print('You got it right')
        break
    elif program_guess < user_number:
        print('your guess is too low')
    elif program_guess > user_number:
        print('Your guess is too high')
    else:
        print('no valid input entered')
    num_of_guesses += 1

print('You took a total guess of' , num_of_guesses)















