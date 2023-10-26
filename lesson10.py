# Task 1

def oops():
    raise IndexError("This is an IndexError")

def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except KeyError as e:
        print(f"Caught a KeyError: {e}")

catch_error()


# Task 2

def square_divide():
    try:
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
        
        result = (a ** 2) / b
        return result
    
    except ValueError:
        print("Input values must be valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

result = square_divide()
if result is not None:
    print(f"The result is: {result}")

