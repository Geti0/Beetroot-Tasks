# Task 1

import random

random_numbers = []
count = 0

while count < 10:
    random_numbers.append(random.randint(1,20))
    count += 1

max_num = random_numbers[0]
index = 1

while index < len(random_numbers):
    if random_numbers[index] > max_num:
        max_num = random_numbers[index]
    index += 1

print("List of random numbers: ", random_numbers)
print("The largest number of the list is: ", max_num)

# Task 2