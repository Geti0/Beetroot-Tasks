# Task 1
def with_index(iterable, start=0):
    current_index = start
    for element in iterable:
        yield current_index, element
        current_index += 1


my_list = ['apple', 'banana', 'orange']
for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")


# Task 2

def in_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    current_value = start
    while (step > 0 and current_value < end) or (step < 0 and current_value > end):
        yield current_value
        current_value += step

for i in in_range(5):
    print(i)

for i in in_range(1, 10, 2):
    print(i)



# Task 3

class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current_value < self.end) or (self.step < 0 and self.current_value > self.end):
            value = self.current_value
            self.current_value += self.step
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        if self.step > 0:
            calculated_value = self.start + index * self.step
            if calculated_value < self.end:
                return calculated_value
            else:
                raise IndexError("Index out of range")
        elif self.step < 0:
            calculated_value = self.start - index * abs(self.step)
            if calculated_value > self.end:
                return calculated_value
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("Step cannot be zero")


my_iterable = MyIterable(1, 10, 2)


for value in my_iterable:
    print(value)


print(my_iterable[0])
print(my_iterable[1])
print(my_iterable[2])

