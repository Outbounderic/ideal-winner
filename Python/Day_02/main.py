# Subscripting is the coutning from 0
# print("Hello"[0])

# int
print("Welcome to the tip calculator.")
total = int(input("What is the bill total? "))

# float
# 3141.59

# boolean
# True
# False

# Pay attention to type errors
# num_char = len(input("Enter a number."))
# numbers dont have len()
# Type conversion is very easy with python

# Mathematical Operations
# 3 + 5
# 5 - 2
# 3 * 2
# 6 / 2 (Division always returns a float)
# 2 ** 2 (Power of 2)
# PEMDAS is true

# Number manipulation
# print(round(8 / 3, 2))
# print(8 // 3) this action floors the number
# += , -=

# This is an f string, they rock.
# print(f"Your total is {total}")

tipPercentage = int(input("What percentage tip would you like to leave? 10, 15, 20, or 25 : "))
totalPeople = int(input("How many people are eating with you today? "))
print(f"Each person should pay: {round((total * (tipPercentage/100)) / totalPeople)}")