# python program to create simple calculator

# some steps to create calculator
 
# 1 . functions for operations
# 2 . user input
# 3 . print result

# step - 1
# 1 . function to add two numbers
def add(num1 , num2):
    return num1 + num2

# 1 . function to substract two numbers
def substract(num1 , num2):
    return num1 - num2

# 1 . function to multiply two numbers
def multiply(num1 , num2):
    return num1 * num2

# 1 . function to division two numbers
def division(num1 , num2):
    return num1 / num2

# 1 . function to average two numbers
def average(num1 , num2):
    return (num1 + num2)/2

# step - 2
# 2 . user input
print("Please select option for calculate:\n" \
    "1. Addition\n" \
    "2. Substraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Average")
select = int(input("Select a option from 1,2,3,4,5 : "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# step - 3
# 3 . print result

if select == 1:
    print(number1 , "+" , number2 , "=" , \
         add(number1 , number2))

elif select == 2:
    print(number1 , "-" , number2 , "=" , \
         substract(number1 , number2))

elif select == 3:
    print(number1 , "*" , number2 , "=" , \
         multiply(number1 , number2))

elif select == 4:
    print(number1 , "/" , number2 , "=" , \
         division(number1 , number2))

elif select == 5:
    print("(", number1 , "+" , number2 , ")" , "/" , "=" , \
    average(number1 , number2))

