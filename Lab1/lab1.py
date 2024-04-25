# 1- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
# first_name = input("Enter Your First Name\n")
# last_name = input("Enter Your Last Name\n")

# print(last_name + " " + first_name)

# _______________________________________________________________________________
# 2- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# n = int(input("Sample value of n is: "))
# result = n + int(str(n) * 2) + int(str(n) * 3)
# print("Expected Result", result)

# _______________________________________________________________________________
# 3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print('''
#       Sample string:
#       a string that you "don't" have to escape
#       This
#       is a ....... multi-line
#       heredoc string --------> example
#       ''')

# _______________________________________________________________________________
# 4- Write a Python program to get the volume of a sphere with radius 6.
# import math


# r = 6
# volume = (4/3)*math.pi*(r**3)
# print("volume of a sphere", volume)

# _______________________________________________________________________________
# 5- Write a Python program that will accept the base and height of a triangle and compute the area.
# base = int(input("Enter base value\n"))
# height = int(input("Enter height value\n"))
# triangle_area = (1/2)*base*height
# print("Triangle Area = ",triangle_area)

# _______________________________________________________________________________
# 6- Write a Python program to construct the following pattern, using a nested for loop. Search about method
# end=””
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# max_stars = 5
# for i in range(1, max_stars * 2):
#     if i <= max_stars:
#         for j in range(i):
#             print("*", end=" ")
#     else:
#         for j in range(max_stars * 2 - i):
#             print("*", end=" ")
#     print()

# _______________________________________________________________________________
# 7- Write a Python program that accepts a word from the user and reverse it.
# word = input("Enter a word\n")
# reversed_word = word[::-1]
# print(reversed_word)

# _______________________________________________________________________________
# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(6):
#         if(i==3 or i==6):
#                 continue;
#         print(i)

# _______________________________________________________________________________
# 9-Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it. Expected Output : 1 1 2 3 5 8 13 21 34

# Function to generate Fibonacci series up to a certain limitdef fibonacci_series(limit):
# Initialize the first two numbers in the sequence    a, b = 0, 1
# fibonacci_list = []
# while a <= limit:
# fibonacci_list.append(a)
# a, b = b, a + b
#     return fibonacci_list
# Set the limitlimit = 50
# fibonacci_list = fibonacci_series(limit)
#     print(num, end=" ")

# _______________________________________________________________________________
# 10- Write a Python program that accepts a string and calculate the number of digits and letters.
# sentence = input("Enter a sentence\n")
# num_of_digits = 0
# num_of_letters = 0

# for char in sentence:
#     if char.isdigit():
#         num_of_digits += 1
#     elif char.isalpha():
#         num_of_letters += 1

# print("Number of digits in sentence: ", num_of_digits)    
# print("Number of letters in sentence: ", num_of_letters)
