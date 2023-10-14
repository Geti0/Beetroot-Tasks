# Task 1
def manipulate_string(input_str):
    if len(input_str) < 2:
        return ''  
    else:
        first_two = input_str[:2]  
        last_two = input_str[-2:]  
        result = first_two + last_two  
        return result


string1 = 'helloworld'
result1 = manipulate_string(string1)
print(f"Sample String: '{string1}'\nExpected Result: '{result1}'")

string2 = 'my'
result2 = manipulate_string(string2)
print(f"Sample String: '{string2}'\nExpected Result: '{result2}'")

string3 = 'x'
result3 = manipulate_string(string3)
print(f"Sample String: '{string3}'\nExpected Result: '{result3}'")


# Task 2

phone_number = input('Enter your phone number: ')

if phone_number.isdigit() and len(phone_number) == 10:
    print('Your input is a valid phone number ')
else:
    print('The input is not a valid phone number. It should contain 10 numerical characters.')

# Task 3

name = 'getuar'

input_name = input('Write the name: ')

if input_name.lower() == name:
    print('True')
else:
    print('False')