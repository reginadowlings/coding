# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year
#  that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore
#   be out of date the next year)

name= input('What is your name: ')
print('My name is ' + name)

age= input('How old are you now?')
print('I am ' + age + ' years old.') 

later_age = 2022 - int(age) + 100
print('You will be ' + str(100) +' years old in the year '+ str(later_age))


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

num= input('Give me a number: ')
mod= int(num) % 4
if mod > 0:
    print('You picked an odd number')
else:
    print('It is an even number. ')


# write a program that prints out all the elements of the list that are less than 5.
a= [1, 0, 3, 2, 4, 4.1, 5, 56,23]
for x in a:
    if x <= 5:
        print(x)


# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
user_input = int(input())

list_of_num_to_divide = range(1, user_input+1) 
for num in list_of_num_to_divide:
    if user_input % num == 0:
        print(num)

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is 
# stored in spam.
spam = 1

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')

def is_short(numbers):
    # your code here
    numbers= [1,3,5,]
    if len(numbers) == 3:
        return True
    else:
        return False



def second_item(l):
    l[0] = -1
    if len(l) ==0 or len(l)==1:
        return len(l)
    else:
        return False



    