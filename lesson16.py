# Task 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def get_salary(self):
        return self.salary

student = Student("Getuar", 16, "10th")
student.study()

teacher = Teacher("Getuar", 35, 80000, "Mathematics")
teacher.teach()
print(f"{teacher.name}'s salary is: {teacher.get_salary()}")


# Task 2

class Mathematician:
    def square_nums(self, numbers):
        return [num ** 2 for num in numbers]

    def remove_positives(self, numbers):
        return [num for num in numbers if num <= 0]

    def filter_leaps(self, years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]



# Task 3

class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}  # Use a dictionary to store products
        self.income = 0

    def add(self, product, amount):
        if isinstance(product, Product):
            if product.name in self.products:
                self.products[product.name][0] += amount
            else:
                self.products[product.name] = [amount, product.price]
        else:
            raise ValueError("Invalid product")

    def set_discount(self, identifier, percent, identifier_type='name'):
        for name, info in self.products.items():
            if (identifier_type == 'name' and name == identifier) or (identifier_type == 'type' and info[1] == identifier):
                info[1] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name in self.products and self.products[product_name][0] >= amount:
            self.products[product_name][0] -= amount
            self.income += self.products[product_name][1] * amount
        else:
            raise ValueError("Product not available in the required quantity")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name][0])
        else:
            raise ValueError("Product not found")

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)




# Task 4

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
        self.log_error()

    def log_error(self):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {self.msg}\n")

try:
    raise CustomException("This is a custom exception message")
except CustomException as ce:
    print("CustomException raised:", ce)


