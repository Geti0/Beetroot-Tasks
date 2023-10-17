# # Task 1

import random

random_num = random.randint(1,10)

print("The random number generated is: ", random_num)

# Task 2

name = input("Name: ")
age = input("Age: ")
age = int(age)

print(f"Hello {name}, on your next birthday you’ll be {age+1} years")


# Task 3

import random

def generate_random_string(input_string):
    # Convert the input string to a list of characters
    char_list = list(input_string)
    
    # Shuffle the characters to create a random string
    random.shuffle(char_list)
    
    # Join the shuffled characters to form the random string
    random_string = ''.join(char_list)
    return random_string

def main():
    input_string = input("Enter an input string: ")
    
    # Generate and print 5 random strings
    for _ in range(5):
        random_string = generate_random_string(input_string)
        print(random_string)

if __name__ == "__main__":
    main()


# Task 4

import random

def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2, num1 + num2

def main():
    num1, num2, correct_answer = generate_math_problem()
    print(f"Let's solve a math problem:")
    print(f"What is {num1} + {num2}?")
    
    try:
        user_answer = int(input("Enter your answer: "))
        if user_answer == correct_answer:
            print("Correct! You got it right.")
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
