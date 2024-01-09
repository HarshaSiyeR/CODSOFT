# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def sub(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multi(num1, num2):
	return num1 * num2

# Function to divide two numbers
def div(num1, num2):
	return num1 / num2

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))


if select == 1:
	print(num1, "+", num2, "=", add(num1, num2))

elif select == 2:
	print(num1, "-", num2, "=", sub(num1, num2))

elif select == 3:
	print(num1, "*", num2, "=", multi(num1, num2))

elif select == 4:
	print(num1, "/", num2, "=", div(num1, num2))
 
else:
	print("Invalid input")

