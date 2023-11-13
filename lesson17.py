# Task 1

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Woof Woof")

class Cat(Animal):
    def talk(self):
        print("Meow")

def make_animal_talk(animal_instance):
    animal_instance.talk()


dog_instance = Dog()
cat_instance = Cat()

make_animal_talk(dog_instance)
make_animal_talk(cat_instance)



# Task 2

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthday={self.birthday})"

    def __str__(self):
        return f"{self.name} ({self.birthday}), {self.country}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author})"

    def __str__(self):
        return f"{self.name} ({self.year}), by {self.author.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name={self.name}, books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name}, Total Books: {Book.total_books}"


# Task 3


from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __repr__(self):
        return f"Fraction({self.numerator}/{self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for +: Fraction and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for -: Fraction and {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for *: Fraction and {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type for /: Fraction and {}".format(type(other)))

# Example usage:
x = Fraction(1, 2)
y = Fraction(1, 4)

result = x + y
print(result)  # Output: 3/4



