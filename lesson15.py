# Task 1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and i'm {self.age} years old")


person = Person('Getuar', 'Kelmendi', 20)
person.talk()


# Task 2
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor


dog = Dog(5)
print(dog.human_age())


# Task 3

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, channel_number):
        if 1 <= channel_number <= len(self.channels):
            self.current_channel_index = channel_number - 1
            return self.current_channel()
        else:
            return "Invalid channel number"

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        else:
            return "Invalid input"


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")
