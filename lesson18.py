# Task 1
import re

class MyClass:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

# Example usage:
try:
    obj = MyClass("example@email.com")
    print("Email is valid!")
except ValueError as e:
    print(f"Error: {e}")

try:
    invalid_obj = MyClass("invalid_email")
    print("This won't be printed because of the exception")
except ValueError as e:
    print(f"Error: {e}")


# Task 2

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Can only add instances of Worker to the workers list")

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss=None):
        self._id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if new_boss is None or isinstance(new_boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            self._boss = new_boss
            if new_boss:
                new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss or None")


boss1 = Boss(1, "Boss1", "CompanyA")
worker1 = Worker(101, "Worker1", "CompanyA", boss1)

boss2 = Boss(2, "Boss2", "CompanyB")
worker2 = Worker(102, "Worker2", "CompanyB", boss2)

worker1.boss = boss2

print(boss1.workers)
print(boss2.workers)


# Task 3

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to int")

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, bool):
                return result
            elif isinstance(result, str):
                if result.lower() == 'true':
                    return True
                elif result.lower() == 'false':
                    return False
                else:
                    raise ValueError(f"Cannot convert {result} to bool")
            else:
                raise ValueError(f"Cannot convert {result} to bool")

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to float")

        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True

