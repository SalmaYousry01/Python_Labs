# 1- Given a list of numbers, create a function that returns a list where all similar adjacent elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.

# def delete_adjacent_duplicates(input_list):
#     new_list = [
#     for i in range(len(input_list)):
#         if i == 0 or input_list[i] != input_list[i - 1]:
#             new_list.append[input_list[i]]
#     return new_list

# __________________________________________________________________________________________________________________
# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half. E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)

# def divide_string(input_string):
#     length = len(input_string)
#     midpoint = length // 2
#     if length % 2 == 0:
#         front_half = input_string[:midpoint]
#         back_half = input_string[midpoint:]
#     else:
#         front_half = input_string[:midpoint + 1]
#         back_half = input_string[midpoint + 1:]
#     return front_half, back_half

# def merge(a, b):
#     a_front, a_back = divide_string(a)
#     b_front, b_back = divide_string(b)

#     result = a_front + b_front + a_back + b_back
#     return result

# __________________________________________________________________________________________________________________
# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

# def check_uniqueness(numbers):
#     unique_numbers = set(numbers)
#     return len(numbers) == len(unique_numbers)

# __________________________________________________________________________________________________________________
# 4- Given unordered list, sort it using algorithm bubble sort
# ( read about  bubble sort and try to implement it)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# __________________________________________________________________________________________________________________
# 5- Gusses game
# ●   Your game generates a random number and gives only 10 tries for the user to guess that number.
# ●   Get a user input and compare it with the random number
# ●   Display a hit message to the user in case the use number is smaller or bigger of the random number
# ●   If the user type number is out of range(100), display a message that is not allowed and don’t count this as try.
# ●   If user type a number that has been entered before, display a hint message and don’t count this as try
# ●   In case the user entered a correct number within the 10 tries, display a congratulations message and let your application guess another random number with the remain number of tries
# ●   If the user finishes all his tries, display a message to ask him if he wants to play again or not.6- Make account on Hacker-rank for problem solving

# import random
# def play_game():
# random_number = random.randint(1, 100)
# tries = 10
# guessed_numbers = []

# print("Welcome to the Guessing Game!")
# print("I have selected a random number between 1 and 100.")
# print("You have 10 tries to guess it correctly.")

# while tries > 0:
#     guess = input("\nEnter your guess: ")


#     if not guess.isdigit():
#         print("Please enter a valid number.")
#         continue

#     guess = int(guess)


#     if guess < 1 or guess > 100:
#         print("Your guess is out of range (1-100). Try again.")
#         continue


#     if guess in guessed_numbers:
#         print("You have already guessed this number. Try again.")
#         continue


#     tries -= 1
#     guessed_numbers.append(guess)


#     if guess < random_number:
#         print("Your guess is too low. Try again.")
#     elif guess > random_number:
#         print("Your guess is too high. Try again.")
#     else:
#         print("Congratulations! You guessed the correct number:", random_number)
#         if tries > 0:
#             print("Let's play again with a new number.")
#             play_game()
#         return

# print("Sorry, you've run out of tries. The correct number was:", random_number)
# play_again = input("Would you like to play again? (yes/no): ")
# if play_again.lower() == "yes":
#     play_game()
# else:
#     print("Thank you for playing!")

# __________________________________________________________________________________________________________________
# 6- Make account on Hacker-rank for problem solving
# (bonus)
# And try to solve this problem and send me your submission
