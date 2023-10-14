# Task 1

import datetime


name = "Your Name"
current_day = datetime.datetime.now().strftime("%A")  

message1 = f"Good day {name}! {current_day} is a perfect day to learn some Python."


message2 = "Good day {}! {} is a perfect day to learn some Python.".format(name, current_day)


message3 = "Good day %s! %s is a perfect day to learn some Python." % (name, current_day)


print(message1)
print(message2)
print(message3)


# Task 2

firstname = 'Getuar'

lastname = 'Kelmendi'

concatenate = firstname + ' ' + lastname

print('Hey ' + concatenate + ' How are you today ?')


# Task 3

# Define the two numbers in separate variables
a = 10
b = 5

addition_result = a + b
print(f"Addition: {a} + {b} = {addition_result}")

subtraction_result = a - b
print(f"Subtraction: {a} - {b} = {subtraction_result}")

division_result = a / b
print(f"Division: {a} / {b} = {division_result}")

multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")

exponent_result = a ** b
print(f"Exponent (Power): {a} ** {b} = {exponent_result}")

modulus_result = a % b
print(f"Modulus (Remainder): {a} % {b} = {modulus_result}")

floor_division_result = a // b
print(f"Floor Division: {a} // {b} = {floor_division_result}")


