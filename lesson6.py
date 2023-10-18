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

import random

list_1 = []
list_2 = []

count = 0

while count < 10:
    list_1.append(random.randint(1,10))
    list_2.append(random.randint(1,10))
    count += 1


common_list = []
index1 = 0

while index1 < len(list_1):
    index2 = 0
    while index2 < len(list_2):
        if list_1[index1] == list_2[index2] and list_1[index1] not in common_list:
            common_list.append(list_1[index1])
        index2 += 1
    index1 += 1


print("List 1:", list_1)
print("List 2:", list_2)
print("Common List without duplicates:", common_list)