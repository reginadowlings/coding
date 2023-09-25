# name = input()
# age = input()
# print('My name is ', name )
# print(name + ' is ', age )


# def myself(lover,feeling):
#     if lover == 'Appiah'  and feeling == str(50):
#         return 'I hate Appiah'

#     elif lover == 'RM' or feeling == str(100):
#          return 'Saranghae, Namjoon-ssi'
        
#     else:
#         return 'I think there is stil a spark'

# print(myself('RM', '67'))


# def max_health(mode):
#     if mode == 'easy':
#         return 100 
#     elif mode == 'hard':
#         return 35
#     else:
#         return 75
        
# print(max_health('hard'))


# def valid_age(x):
#     if x >= 0 and x <= 150:
#         return True
#     else:
#         return False
        
# print(valid_age(999))

# def decide(price):
#     if price < 100:
#         return 'buy'
#     if price > 100 and price < 150:
#         return 'hold'
#     if price > 150:
#         return 'sell'
        
# decide(106)


# name= input('Enter your name: ')

# while name == '':
#     print('No strings entered')
#     name= input('Enter your name: ')
# else:
#     print(f'Hi there, {name}')

    
# num = [1,2,3,4,5,6,7,8]

# for n in num:
#     if n == 5:
#         print('found!')
#         continue
#     print(n)


# items_to_share = 25
# people =  5

# print( items_to_share % people)

# name= 'stephen'
# index = 0
# for n in name:
#     print(n, 'is at index', index)
#     index +=1


# secs_in_a_day = 3600 * 24

# secs_in_a_week= secs_in_a_day * 7

# print('there are', secs_in_a_week, 'in a week' )


# The cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping costs $3 for the first copy and 75 cents for
# each additional copy. Calculate the total wholesale costs for 60 copies.

# cover_price = 24.95 * 60
# discount_amt = (40/100) * cover_price
# discount= cover_price - discount_amt

# shipping_cost = 3 + (59 * 0.75)


# total_cost = discount + shipping_cost 
# print(total_cost)


# You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time will the alarm go 
# off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator.
# alarm_off = (14 +535) % 24
# print(alarm_off,'.00')


'''Define three variables var1, var2 and var3. Calculate the average of these variables and assign it to average. Print the average. 
Add three comments.'''

# let\'s assign even numbers to the variables
# average calculates as the sum of given numbers over the total numbers in the set
# i hope this code works

# var1 = 2 
# var2 = 4
# var3 = 6
# average= (var1 + var2 + var3) / 3
# print(average)


'''Write code that can compute the surface of circle, using the variables radius and pi = 3.14159. The formula, in case you do not know,
is radius times radius times pi. Print the outcome of your program as follows: “The surface area of a circle with radius ...is ..'''
# radius = 7
# pi = 3.14159
# surface_area = (radius ** 2) * pi

# print('The surface area of a circle with radius', 7, 'is ', surface_area)


'''Can you think of a way to swap the values of two variables that does notneed a third variable as a temporary storage? In the code 
block below, try to implement the swapping of the values of a and b without using a third variable. To help you out, the first step 
to do this is already given. You just need to add two more lines of code.'''

# a = 17
# b = 23

# temp = a
# a = b
# b = temp


'''Write code that classifies a given amount of money (which you store in a variable named amount), specified in cents, as greater monetary
units. Your code lists the monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and pennies (1 ct). 
Your program should report the maximum number of dollars that fit in the amount, then the maximum number of quarters that fit in the 
remainder after you subtract the dollars, then the maximum number of dimes that fit in the remainder after you subtract the dollars and 
quarters, and so on for nickels and pennies. The result is that you express the amount as the minimum number of coins needed.'''



'''Write some code that asks the user for two numbers, then shows the result when you add them, and when you multiply them.'''

# num1 = int (input('give me an even number: '))
# num2 = int (input('give me an odd number:'))

# print(num1 + num2)
# print(num1 * num2)

# print( "X", "X", "X", sep="x" )
# print( "X", end="" )
# print( "Y", end="" )
# print( "Z" )

# print(len('can\'t' ))

# num = 7/11
# print(num )

name = 'Regina'
age = 23
'''print (f'Her name is {name} and she turned {age} last year')'''

# print('She turned {1} last year, I mean {0}'.format(name, age))

# my_age = 23
# print (f'I will be {my_age} this year')

# print( "Backwards they are {2}, {1} and {0}.".format("one", "two", "three" ) )

# print( "The first 3 numbers are {}, {} and {}.".format("one", 2, 3.0 ) )
'''
print( "The first 3 numbers are {:7}, {:7} and {:7}.".format("one", "two", "three" ) )'''


# print( "{} divided by {} is {}".format( 1, 2, 1/2 ) )
# print( "{:d} divided by {:d} is {:f}".format( 1, 2, 1/2 ) )
# print( "{:.1f} divided by {:.1f} is {:.2f}".format( 1, 2, 1/2 ) )

# print( "{:5d} divided by {:5d} is {:5f}".format( 1, 2, 1/2 ) )
# print( "{:<5f} divided by {:^5f} is {:>5f}".format( 1, 2, 1/2 ) )

# s = "{:>5d} times {:>5.2f} is {:>5.2f}"
# print( s.format( 1, 3.75, 1 * 3.75 ) )
# print( s.format( 2, 3.75, 2 * 3.75 ) )
# print( s.format( 3, 3.75, 3 * 3.75 ) )
# print( s.format( 4, 3.75, 4 * 3.75 ) )
# print( s.format( 5, 3.75, 5 * 3.75 ) )

# agi = 'The {:3} daughter is {:>10} and she is {:^7.1f} years old'
# print(agi.format('Dowlings', 'Aurie', 25))
# print(agi.format('Dowlings', 'Gina', 23))
# print(agi.format('Dowlings', 'Githa', 23))
# print(agi.format('Dowlings', 'Cathy', 22))
'''
from math import sqrt
print( sqrt( 4 ) )



from math import exp , log

print( "The value of e is approximately",  exp (1 ), 1)

e_sqr = exp( 2 )
print( "e squared is", e_sqr )
print( "which means that log(", e_sqr , ") is", log( e_sqr ) )'''

# from random import random, randint

# # print(random())
# print(randint(2,9))

'''from random import random , randint , seed
seed()
print( "A random number between 1 and 10 is", randint( 1, 10 ) )
print( "Another is", randint( 1, 10 ) )
seed( 0 )
print( "3 random numbers are:", random(), random(), random() )
seed( 0 )
print( "The same 3 numbers are:", random(), random(), random() )'''


'''Ask the user to enter a string. Then print the length of that string. Use the input() function rather that the getString() function 
from pcinput, as the getString() function removes leading and trailing spaces.'''


# The Pythagorean theorem states that of a right triangle, the square of the length of the diagonal side is equal to the sum of the 
# squares of the lengths of the other two sides (or a2 + b2 = c2). Write a program that asks the user for the lengths of the two sides
# that meet at a right angle, then calculate the length of the third side (in other words: take the square root of the sum of the squares
#  of the two sides that you asked for), and display it in a nicely formatted way. You may ignore the fact that the user can enter
# negative or zero lengths for the sides.

from math import sqrt 
'''
length_a = int (input('Give me the length of the base: '))
length_b = int(input('Give me the length of the vertical line: '))'''

'''length_of_diagonal = length_a ** 2  + length_b ** 2 '''

'''print('The length of the diagonal side is', sqrt(length_of_diagonal))'''

# Ask the user to enter three numbers. Then print the largest, the smallest, and their average, rounded to 2 decimals.
# num1 = int(input())
# num2 = float(input())
# num3 = int(input())

# print(max(num1, num2, num3))
# print(min(num1, num2, num3))
# print(num1 + num2 + num3 / 3)
# sum = num1+  num2 + num3
# print(round(sum, 2))

'''
Calculate the value of e to the power of -1, 0, 1, 2, and 3, and display the results, with 5 decimals, in a nicely formatted manner'''

from math import exp

a = exp(-1)
b = exp(0) 
c = exp(1)
d= exp(2) 
e = exp(3)

'''print('The value of e is approximately {:.5f}'.format(a) )
print('The value of e is approximately {:.5f}'.format(b) )
print('The value of e is approximately {:.5f}'.format(c) )
print('The value of e is approximately {:.5f}'.format(d) )
print('The value of e is approximately {:.5f}'.format(e) )'''


# Suppose you want to generate a random integer between 1 and 10 (1 and 10 both included), but from the random module you only have the 
# random() function available (you can use functions from other modules, though). How do you do that?
from random import randint
# print(randint(1,10))


from random import random
# print( "A random integer between 1 and 10 is",
# 1 + int( random() * 10 ) )

'''print( "1.", 2 < 5 )
print( "2.", 2 <= 5 )
print( "3.", 3 > 3 )
print( "4.", 3 >= 3 )
print( "5.", 3 == 3.0 )
print( "6.", 3 == "3" )
print( "7.", "syntax" == "syntax" )
print( "8.", "syntax" == "semantics" )
print( "9.", "syntax" == " syntax" )
print( "10.", "Python" != "rubbish" )
print( "11.", "Python" > "Perl" )
print( "12.", "banana" < "orange" )
print( "13.", "banana" < "Orange" )
'''
# greater = 5 > 2
# print( greater )
# greater = 5 < 2
# print( greater )
# print( type( greater ) )

# Write some code that allows you to test if 1/2 is greater than, equal to, or less than 0.5. Do the same for 1/3 and 0.33. 
# Then do the same for (1/3) 3 and 1.
'''print(1/2 > 0.5)
print(1/2 == 0.5)
print(1/2 < 0.5)
print(1/3 > 0.33)
print(1/3 == 0.33)
print(1/3 < 0.33)'''

# print( "y" in "Python" )
# print( "x" in "Python" )
# print( "p" in "Python" )
# print( "th" in "Python" )
# print( "to" in "Python" )
# print( "y" not in "Python" )
 
a = True or False
b = True or False
c = True or False
print( (a and b) or c )
print( a and (b or c) )


# Write a program that defines a variable weight. If weight is greater than 20 (kilo’s), print: “There is a $25 surcharge for luggage 
# that is too heavy.” If weight is smaller than 20, print: “Have a safe flight!” If weight is exactly 20, print: “Pfew! The weight is 
# just right!” Make sure that you change the value of weight a couple of times to check whether your code works.

'''weight = 12 

if weight > 20:
    print('There is a $25 surcharge for luggage that is too heavy')
elif weight < 20:
    print('Have a safe flight!')
elif weight == 20:
    print('Pfew! The weight is just right!')
else:
    print('Please adhere to instructions')'''


# x = 41
# if x % 7 == 0:
# # --- Here starts a nested block of code ---
#     if x%11 == 0:
#         print( x, "is dividable by both 7 and 11." )
# else:
#     print( x, "is dividable by 7, but not by 11." )

# # --- Here ends the nested block of code ---
# x = 41 

# elif x%11 == 0:
#     print( x, "is dividable by 11, but not by 7." )
# else:
#     print( x, "is dividable by neither 7 nor 11." )


first_name = 'regina'
last_name = 'dowlings'

# if first_name == 'regina'  and  last_name == 'dowlings' :
#     print('Hey there, Eyako')
# else:
#     print('you know you can be persecuted for this!')


'''
num = getInteger( "Please enter a positive integer: " )
if num < 0:
print( "You should have entered a positive integer!" )
else:
print( "Now I am processing your integer", num )
print( "Lots and lots of processing" )
print( "Hundreds of lines of code here" )'''


# Grades are values between zero and 10 (both zero and 10 included), and are always rounded to the nearest half point. To translate grades
# to the American style, 8.5 to 10 become an “A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become a “D,” and other grades
# become an “F.” Implement this translation, whereby you ask the user for a grade, and then give the American translation. If the user 
# enters a grade lower than zero or higher than 10, just give an error message. You do not need to handle the user entering grades that
# do not end in .0 or .5, though you may do that if you like – in that case, if the user enters such an illegal grade, give an appropriate
# error message.
'''
grade = float(input("Enter the grade: "))

if grade < 0 or grade > 10:
    print("Error: Grade must be between 0 and 10 (inclusive).")
else:
    rounded_grade = round(grade * 2) / 2  # Round to the nearest half point
    
    if rounded_grade == 10 or rounded_grade >= 8.5:
        print("Grade: A")
    elif rounded_grade >= 7.5:
        print("Grade: B")
    elif rounded_grade >= 6.5:
        print("Grade: C")
    elif rounded_grade >= 5.5:
        print("Grade: D")
    else:
        print("Grade: F")'''




# Ask the user to supply a string. Print how many different vowels there are in the string. The capital version of a lower case vowel is 
# considered to be the same vowel. y is not considered a vowel. Try to print nice output (e.g., printing “There are 1 different vowels in
#  the string” is ugly). Example: When the user enters the string “It’s Owl Stretching Time,” the program should say that there are 3
# different vowels in the string.

'''name = input('what is your name: ')
vowels = 0
if 'a' in name:
    vowels +=1
if 'e' in name :
    vowels += 1
if 'i' in name :
    vowels += 1
if 'o' in name:
    vowels += 1
if 'u' in name:
    vowels +=1

if vowels == 0:
    print('No vowels spotted')
elif vowels == 1:
    print('got one vowels')
else: 
    print('There are', vowels , 'vowels in', name)'''

# Change the code above so that it prints the numbers 1, 3, 5, 7, and 9.
'''
num = 1 
while num <= 10:
    print(num)
    num += 2
print('odd numbers less than 10')'''

'''from pcinput import getInteger
total = 0
count = 0
while count < 5:
    total += getInteger( "Please give a number: " )
    count += 1
print( "Total is", total )'''


# fruit = "banana"
# for letter in fruit:
#     print( letter )
#     if letter == "n":
#         fruit = "orange"
# print( "Done" )



# Use the for loop and range() function to print multiples of 3, starting at 21, counting down to 3, in just two lines of code.

'''for x in reversed (range (3, 21, 3)):
    print(x)'''

'''for x in range( 1, 11, 2 ):
    print( x )'''


# Write countdown code. It starts with a given number (e.g., 10), and counts down to zero, printing each number it 
# encounters (10, 9, 8, ...). It does not print 0, instead it prints “Blast off!”
'''
countdown = 10
while True:
    if countdown == 0:
        break
    print(countdown)
    countdown -=1
print('Blast off')
'''
# using a for loop

'''for i in reversed (range (1,11)):        
    print (i)
print('blast off')'''


'''i = 0
for i in range (1, 51):
    if i == 50:
        break
print(i)
'''

'''for fruit in ( "apple", "orange", "strawberry" ):
    print( fruit )
else:
    print( "The loop ends , fruit is now", fruit )
print( "Done" )


i = 0
while i < 5:
    print( i )
    i += 1
else:
    print( "The loop ends , i is now", i )
print( "Done" )'''

# for grade in ( 8, 7.5, 9, 6, 6, 5.5, 6, 7, 8, 7, 7.5 ):
#     if grade < 7:
#         print( "The student fails!" )
#         break
# else:
#     print( "The student passes!" )

# num = 0
# while num < 100:
#     num += 1
#     if num%2 == 0:
#         continue
#     if num%3 == 0:
#         continue
#     if num%10 == 7:
#         continue
#     if num%10 == 9:
#         continue
#     print( num )

# A Short Program: Guess the Number

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
    print('Nope. The number I was thinking of was ' + str(secretNumber))


from random import randint

secretNumber = randint(1, 10)
print('I am thinking of a number between 1 and 10.')

for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())

 # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))'''


# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is
# stored in spam.

# spam = int(input('Give me a value: '))

# if spam == 1: 
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('GREETINGS!')


# Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers
# 1 to 10 using a while loop.

# for i in range (1,11):
#     print (i)

# i =1
# while i <= 10:
#     print(i)
#     i += 1


# from lesson import add     #this code imports an addition function from another file named lesson.py
'''
numbers = (2, 4, 6)   #this are the numbers to be added 
total = add(numbers)      #call the add function to sum up the numbers
print(total)
'''











