#  Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the
# birthday of that person back to them. 

# people  = {'Gina':'08/10/99', 'Githa':'08/10/99','Aurie':'12/04/94', 'Glah':'21/04.76', 'Steph':'23/07/96'}

# print('Welcome to the birthday dictionary. We have the birthdays of :')
# for key in people:
#     print(key)


# def get_birthday(request):

#     if request in people:
#         value = people[request]
#         print('The birthday of', request, 'is', value) 
#     else:
#         print( 'No valid request entered')
    
# user_key = input('Enter a name from the dictionary provided: ')
# get_birthday(user_key)




#  Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function! 
# All you need is some variables and if statements!

# def get_largest(num):
#     return max(num)

# x,y,z = map(int, input('Enter three numbers: ').split())
# print(get_largest(x,y,z))

# OR 

# def get_largest (num, num1, num2):
#     largest = float('-inf')

#     if num > largest:
#         largest = num 
#     if num1 > largest:
#         largest = num1
#     if num2 > largest:
#         largest = num2 
#     return largest

# num, num1, num2 = map(int, input('Give me three numbers: ').split())
# print('The largest numbers is', get_largest(num, num1, num2))



# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they
# will turn 100 years old), except don’t explicitly write out the year. Use the built-in Python datetime library to make the code you write work 
# during every year, not just the one we are currently in.

# from datetime import datetime

# current_date = datetime.now()                  #this displays the current date and time
# current_year = current_date.strftime('%Y')    #this line of code tells the current year 

# name = input('What is your name: ')   
# age= int(input('How old are you? '))

# year_to_a_cen = 100 - age
# year_turning_100 = int(current_year) + year_to_a_cen

# print(f'{name}, you will turn 100 in the year, {year_turning_100}')














