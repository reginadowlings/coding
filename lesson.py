# This program says hello and asks for name

print('Hello World')
my_name = 'Regina'
print('It is good to meet you ' + my_name )

my_age = 23
result = f'I will be {my_age} this year'
print(result) 
print(int('98'))

print('I am ' + str(29) + ' years old')

print("Welcome to my first program.")
print("Type your name below:")
name= input()
print(f"Hurray, {name}")

print('What is your age')
age= input()
age= int(age)
print(type(age))

print(age+1)

print(int(1.99))

print(age)
print(type(age))
int_age = '22'
print(type(int_age))
print(f'Hi I am {age} years old')

print('What is your age?') # ask for their age
myAge = input()
myAge= str(myAge)
print('You will be ' + myAge  + ' in a year.') 

number= 234.767625
print(round(number,4))

# spam= True
# print(spam)
print(False and False)

a= 42 + 8
b= 8 + 42
print(a == b)
print(not not not  not False)

print(False or False and True)

print(4 > 5  and 4!=8)
print((4 < 5) or (5 < 6))
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)

name = 'Kim'
if name == 'Kim':
    print('hello ' + name)

name = 'Eyako'
password= 'Dowlings.edu'
if name == 'Eyako':
    print('Hi, Eyako')
    if password == 'Dowlings.edu':
     print('Hello there, Eyako. Welcome!')

name= 'Dowlings'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

age= 24
if age == 23:
    print('Hi, I am 23 years old')
else:

 def test_or_long(value):
     if value == "test" or len(value) == 6:
          return True
     else:
          return False

print(test_or_long("yssss"))
#

def namjooning(like, love, hope):
    if like =='reading books' and love == 'admire nature' or hope == ' world artist': 
        return 'The act of Namjooning is therapeutic'
    else:
        return 'Are you a trainee of Jinhit entertainment?'    

print(namjooning('moon', 'tuna', 'artist'))


# # Write a function named make_day_string that takes an integer named day and returns the string "it is day X of the month" where X is the
# #  value of the day parameter.For example, calling make_day_string(3) should return "it is day 3 of the month".Remember that to concatenate
# #   a string with an integer, you must cast the integer to a string.
# #   note that the function should return a value. It should not print anything.

def make_day_string (day):
     result= 'It is the ' + str(day) + ' of the month.'
     return result
print(make_day_string('3'))

     

language = 'ada'

if language == 'Ewe':
     print('You are voltarian')
elif language == 'ada':
     print('which dangme clan are you from?')

else:
     print('which tribe are you?')


name= 'Bangtan'
password= 130613

if name == 'Bangtan' and password == 130613:
     print('Welcome, Army!')
else:
     print('This is Bangtan business, Blink')


def bang_tan(bias, age):
     if bias == 'RM' and age == 29:
          return 'You got daddy issues huh?'

     else:
          return ' Hey there... Yeontan lover'


print(bang_tan('RM', 27))

name = ['reg', 'steph', 'aurie', 'githa']
for item in name:
     print(item)

# lists
# append, extend, remove, insert, sort, reverse

# version 1
# write a program, that generates a random number
# and then ask the user to input a guess
# if the guessed number is the number the program generated, then 
# display, a message
# else: inform the user their guess was wrong.

# version 2
# if the guess was wrong,
# give user 3 hints

# hint 1: tell the user if the correct number is even or odd
# hint 2: tell the user if the number they guessed is greater than or less than the correct number
# hint 3: give the user 3 numbers to choose from. only one of those number is the correct number.

name = 'Carol'
age = 3000
if name == 'Alice':
     print('Hi, Alice.')
elif age < 12:
     print('You are not Alice, kiddo.')
elif age > 100:
     print('You are not Alice, grannie.')
elif age > 2000:
     print('Unlike you, Alice is not an undead, immortal vampire.')

while True:
     print('Please type your name.')
     name = input()
     if name == 'your name':
          break
print('Thank you!')

while True:
     print('Who are you?')
     name = input()
     if name != 'Joe':
          continue
     print('Hello, Joe. What is the password? (It is a fish.)')
     password = input()
     if password == 'swordfish':
          break
print('Access granted.')
''

while True:
     name = input('what is your name: ')
     if name == '':
          name = input('what is your name: ')      
     else:
          print('hi {}'.format(name) )
          break

total = 0
for num in range(101):
     total = total + num
     print(total)

# version 1
# write a program, that generates a random number
# and then ask the user to input a guess in 5 guesses
# if the guessed number is the number the program generated, then 
# display, a message
# else: inform the user their guess was wrong.

from random import randint 
py_guess = randint(1,10)

for attempts in range (1,6):
    print('Guess a number: ')
    user_guess= int(input())

if py_guess == user_guess:
    print('got it!')
else:
    print('wrong guess, I thought of', py_guess)



def add(values):
    '''this function gives a total of the sum of numbers and returns the value'''
    total = sum(values)
    return total

numbers = (1470, 900, 420, 1000)

amt = add(numbers)
print(amt)




