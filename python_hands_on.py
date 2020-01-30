"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO 1
# Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi), pi)


# TODO 2
# Write a conditional to print out if `i` is less than or greater than or equal to 50
i = random.randint(0, 100)
if i < 50:
    print ('i is less than 50')
elif i > 50:
    print ('i is greater than 50')
else:
    print ('i is equal to 50')
# TODO 3
# Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print ('orange')
elif picked_fruit == 'strawberry':
    print ('red')
else :
    print ('yellow')

# TODO 4
# Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2):
    return num1 * num2

# TODO 5
# use `input` function to get 2 number and print the multiply of numbers.
num1 = int(input('enter number1:'))
num2 = int(input('enter number2:'))

print("multiply answer =", multiply(num1, num2))
