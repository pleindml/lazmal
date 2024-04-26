# Assignment
1
# name = input("Enter your name:\n")
# print(f'Good day {name}')

# 2
# num1 = int(input("Enter first number to sum:\n"))
# num2 = int(input("Enter second number to sum:\n"))
# print(f'The sum of the numbers is: { num1 + num2}')

# 3
# first_name = input("Enter your first name\n")
# second_name = input("Enter your second name:\n")
# age = input("Enter your age too:\n")
# print(f'Good day {first_name} {second_name}, I see you are {age} years old')

# 4
# favorite_color = input("Enter your favorite color:\n")
# favorite_animal = input("Enter your favorite animal:\n")
# print("Your favorite color and animal is" +  ' ' + favorite_color + ' ' + "and" + ' ' + favorite_animal + "?, eww")

# 5
import datetime
from datetime import datetime
# first_name = input("Enter your first name\n")
# birth_year = int(input("Enter your birthyear:\n"))
# current_year = datetime.now().year
# print(f'Good day {first_name}, I see you are about {current_year - birth_year} years old')

# 6
# hometown = input("Enter your hometown:\n")
# favorite_food = input("Enter your favorite food:\n")
# print("Your hometown is" + ' ' + hometown + ' ' + "and your favorite food is" +  ' ' + favorite_food)

# 6b


# 7
# visited_city = input("Which city did you visit:\n")
# year_visit= input("What is the year of visit?:\n")
# print("You visited" + ' ' + visited_country + ' ' + "and the year was" +  ' ' + year_visit)

# 8
# movie_name = input("Enter the name of the movie you watched:\n")
# movie_year_release = int(input("What year did you watch it?:\n"))
# print(f'You watched {movie_name} and the year you watched it was {movie_year_release}')

# 9
# fruit_name = input("Enter the name of your favorite fruit:\n")
# fruit_consumption = int(input("How many times do you eat it in a week?:\n"))
# print(f'You like eating {movie_name} and you eat it {movie_year_release} per week')

# 10
# favorite_subject = input("Enter the name of your favorite subject in school:\n")
# grade_level = int(input("What is your grade level?:\n"))
# print(f'Your favorite subject {favorite_subject} an your grade level is {grade_level}')

# 11
# favorite_sport = input("Enter the name of your favorite sport in school:\n")
# sport_season = int(input("What season do you play it?:\n"))
# print(f'Your favorite sport {favorite_sport} and season you play it is {sport_season}')

# Assignment
# 1.What is the syntax for creating an empty list in Python?
# my_list = list()

# 2.How do you access the third element in a list named my_list?
# my_list = ["orange", "apple", "cake"]
# print(my_list[2])

# 3.Write a Python code snippet to add an element 'apple' to the end of a list named fruits.


# 4.How do you remove the third element from a list named numbers?

# 5.Explain the difference between the append() and extend() methods in Python lists.

# 6.Write a Python code snippet to check if an element 'banana' exists in a list named fruits.

# 7. What will be the output of len(['a', 'b', 'c'])?

# 8. How do you reverse the order of elements in a list named my_list?

# 9.Explain the purpose of the sort() method in Python lists.

# 10.Write a Python code snippet to create a list containing the squares of numbers from 

# 11. What is a string in Python?

# 12. How do you create an empty string?

# 13. Can you access characters in a string using indexing?

# 14. How do you find the length of a string?

# 13. How do you concatenate two strings?

# 14. How do you convert a string to uppercase?

# 15. How do you convert a string to lowercase?

# 16. How do you check if a substring exists in a string?

# 17. How do you make a string into a list of substrings?

# 18. How do you replace occurrences of a substring within a string?

# 19. How do you find the index of a substring within a string?

# 20. How do you iterate over the characters of a string?

# 21. How do you reverse a string in Python?

# 22. How do you convert an integer or float to a string?

# 23. How do you check if a string contains only digits?

# 24. Write a Python code snippet to create an empty list.

# 25. How do you add an element to the end of a list in Python?

# 26. Explain the difference between append() and extend() methods in Python lists.

# 27. Write a Python function to find the sum of all elements in a list of numbers.

# 28. Given a list [1, 3, 5, 7, 9], write a Python code snippet to access the third element of the list.

# 29. Write a Python function to find the maximum and minimum elements in a list of numbers.

# 30. Explain the concept of list comprehension in Python with an example.

# 31. How do you check if a specific element exists in a list in Python?

# 32. how do you reverse a list.


# Example tuple
# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# element = 3

# # Function to check if a given tuple is empty
# is_empty_tuple = len(tup1) == 0
# print("Is tuple empty:", is_empty_tuple)

# # Program to find the length of a tuple
# tuple_length = len(tup1)
# print("Length of tuple:", tuple_length)

# # Program to reverse a tuple
# reverse_tuple = tup1[::-1]
# print("Reversed tuple:", reverse_tuple)

# # Function to check if a given element exists in a tuple
# element_exists = element in tup1
# print("Does element exist in tuple:", element_exists)

# # Program to convert a tuple to a list
# tuple_to_list = list(tup1)
# print("Converted tuple to list:", tuple_to_list)

# # Program to find the maximum and minimum elements in a tuple
# max_element = max(tup1)
# min_element = min(tup1)
# print("Maximum element in tuple:", max_element)
# print("Minimum element in tuple:", min_element)

# # Program to concatenate two tuples
# concatenated_tuple = tup1 + tup2
# print("Concatenated tuple:", concatenated_tuple)

# # Find the sum of all elements in the numbers tuple:
# numbers_tuple = (1, 2, 3, 4, 5)
# total_sum = sum(numbers_tuple)
# print("Sum of all elements in the numbers tuple:", total_sum)

# # Program to remove an element from a tuple
# remove_element = tuple(i for i in tup1 if i != element)
# print("Tuple after removing element:", remove_element)

# # Program to find the index of a particular element in a tuple
# element_index = tup1.index(element) if element in tup1 else -1
# print("Index of element in tuple:", element_index)

# 1.Write a Python program to check if a given number is even and divisible by 3 using if and else statements. if the number is even print BUZZ if the number is divisible by three let it print FIZZ

# num = 6
# if num % 2 == 0:
#     print("BUZZ")
# elif num % 3 == 0:
#     print("FIZZ")
# else:
#     print("Neither BUZZ nor FIZZ")

# 2.Create a program that asks the user to input their age and then outputs whether they are eligible to vote or not using if and else.

# age = int(input("Enter your age to see if you can vote:\n"))
# if age >= 18:
#     print("You are allowed to vote")
# else:
#     print("You are not the required age to vote, vote when you are 18 and above")

# 3.Write a Python program that takes a user input for a number and prints "Positive" if it's greater than zero, "Negative" if it's less than zero, and "Zero" if it's equal to zero using if, elif, and else.

# num = int(input("Enter a number:\n"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else: 
#     print("Zero")

# 4. Create a program that print multiplication table when a user input any number using while loop and for loop

# num = int(input("Enter a number to print multiplication table:\n"))
# print("Multiplication table using while loop:")
# i = 1
# while i <= 12:
#     print(f"{num} x {i} = {num * i}")
#     i += 1
# print("\nMultiplication table using for loop:")  
# for i in range(1, 13):
#     print(f"{num} x {i} = {num * i}")    

# 5. Write a Python program that compares two numbers provided by the user and prints the larger number using if and else.

# num1= int(input("Enter first number:\n"))
# num2= int(input("Enter second number:\n"))

# if num1 > num2:
#     print(f"The larger number is {num1}")
# else:
#     print(f"The larger number is {num2}")

# 6. Create a program that takes a user input for a grade such that grade between 90 - 100 should print Grade A, grade between 70 - 89 should print Grade B, grade between 50 - 69 should print Grade C, grade between 40 - 49 should print  Fail and grade between 0 to 39 should print unknown Results. 

# grade = int(input("Enter your score:\n"))
# if grade >= 90 and grade <= 100: 
#     print("Grade A")
# elif grade >= 70 and grade <= 89:
#     print("Grade B")
# elif grade >= 50 and grade <= 69:
#     print("Grade C")
# elif grade >= 40 and grade <= 49:
#     print('Fail')
# elif grade >= 0 and grade <= 39:
#     print("Unknown Results")
# else:
#     print("Invalid grade entered")

# 7. Write a program that asks the user to input their salary and then calculates their tax based on the following conditions: if salary is less than or equal to 5000, tax is 10%; if salary is between 5001 and 10000, tax is 20%; otherwise, tax is 30% using if, elif, and else.

# salary = int(input("Enter your salary:\n"))
# tax10 = salary * 10/100
# tax20 = salary * 20/100
# tax30 = salary * 30/100
# if salary <= 5000: 
#     print(f"Tax is {tax10}")
# elif salary >= 5001 and salary <= 10000:
#     print(f"Tax is {tax20}")
# else:
#     print(f"Tax is {tax30}")

# 8.Create a program that asks the user to input two numbers and then checks if their sum is greater than 100. If it is, print "Sum is greater than 100", otherwise print "Sum is not greater than 100" using if and else.

# num1= int(input("Enter first number:\n"))
# num2= int(input("Enter second number:\n"))
# sum = num1 + num2
# if sum > 100:
#     print(f"Sum is greater than 100")
# else:
#     print(f"Sum is not greater than 100")

# 9.Write a Python program that takes three numbers from the user and prints the largest among them using nested if-else statements.

# num1= int(input("Enter first number:\n"))
# num2= int(input("Enter second number:\n"))
# num3= int(input("Enter third number:\n"))
# if num1 >= num2:
#     if num1 >= num3:
#         largest = num1
#     else:
#         largest = num3
# else:
#     if num2 >= num3:
#         largest = num2
#     else:
#         largest = num3
# print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest)

# 10. Create a program that takes a user input for their age and then checks if they are eligible for a senior citizen discount (age 60 or above). If they are eligible, print "You are eligible for a senior citizen discount", otherwise print "You are not eligible for a senior citizen discount" using if and else

# age = int(input("Enter your age to check if they are eligible for a senior citizen discount (age 60 or above):\n"))
# if age >= 60:
#     print("You are eligible for a senior citizen discount")
# else:
#     print("You are not eligible for a senior citizen discount")

# 11. create a program for a guessing game when the user guess right it should tell the user that your are right with a congratulation message printed and if the user get it wrong the user should be ask to conttinue trying till the user get the game right

# import random
# while True:
#     x = random.randint(1, 6)
#     num1 = int(input("Guess the number: \n"))
#     if num1 == x:
#         print("Congratulations you guessed right")
#         break
#     else:
#         print(f"Wrong!, Try again the number was {x}")

# word = ["Training", "Mango", "Tech", "Rock", "technicial", "software", "Analysis", "togo"
# "Tonga" ]
# 1. bring out the word that start with both capital letter T and small letter t
# words_T = [word for words in word if words.startswith("T") or words.startswith("t")]
# print(words_T)

# person = [
# {
# "name":"Emeka",
# "email":"emeka@gmail.com",
# "country":["United States", "Canada", "Thailand", ["Ghana", "Morocco", "Germany"]]
# },
# {
# "name":"John",
# "email":"emeka@gmail.com",
# "country":["South Africa", "Congo", "", ["Senegal", ["Digital", ["Fortress"], "Software"],"China", "Data"]]
# },
# {
# "name":"Joy",
# "email":"emeka@gmail.com",
# "country":"Nigeria"
# },
# ]
# print(person[0]["country"][3][0])
# print(person[1]["country"][3][1][0])
# print(person[1]["country"][3][1][1][0])
# from the above data:
# i. bring print out Ghana
# ii. print out Digital
# iii. print out fortress

# balance = 0

# def check_balance():
#     print("Your current balance is: ${}".format(balance))

# def deposit(amount):
#     global balance
#     balance += amount
#     print("${} deposited successfully.".format(amount))
#     check_balance()

# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         balance -= amount
#         print("${} withdrawn successfully.".format(amount))
#         check_balance()
#     else:
#         print("Insufficient funds. Your current balance is ${}".format(balance))

# while True:
#     print("\nOptions:")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Quit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == '1':
#         check_balance()
#     elif choice == '2':
#         amount = float(input("Enter deposit amount: $"))
#         deposit(amount)
#     elif choice == '3':
#         amount = float(input("Enter withdrawal amount: $"))
#         withdraw(amount)
#     elif choice == '4':
#         print("Thank you for using the ATM. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")


# balance = 0

# while True:
#     print("\nOptions:")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Quit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == '1':
#         print("Your current balance is: ${}".format(balance))
#     elif choice == '2':
#         amount = float(input("Enter deposit amount: $"))
#         balance += amount
#         print("${} deposited successfully.".format(amount))
#         print("Your current balance is: ${}".format(balance))
#     elif choice == '3':
#         amount = float(input("Enter withdrawal amount: $"))
#         if balance >= amount:
#             balance -= amount
#             print("${} withdrawn successfully.".format(amount))
#             print("Your current balance is: ${}".format(balance))
#         else:
#             print("Insufficient funds. Your current balance is ${}".format(balance))
#     elif choice == '4':
#         print("Thank you for using the ATM. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")

balance = 0

while True:
    print("\nOptions:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter deposit amount: $"))
        balance += amount
        print(f"${amount} deposited successfully.")
        print(f"Your current balance is: ${balance}")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: $"))
        if balance >= amount:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
            print(f"Your current balance is: ${balance}")
        else:
            print(f"Insufficient funds. Your current balance is ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
