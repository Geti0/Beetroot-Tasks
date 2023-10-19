# Task 1

def favorite_movie(movie):
    print(f'My favorite movie is named {movie}')

favorite_movie('John Wick')

# Task 2

def make_country(country_name, country_capital):
    country_info = {
        'names' : country_name,
        'capital' : country_capital
    }
    print(country_info)

make_country("Kosova", "Shqiperia")


# Task 3

def make_operation(operator, *args):
    result = 0
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
    return result

print(make_operation('+', 7, 7, 2))  
print(make_operation('-', 5, 5, -10, -20)) 
print(make_operation('*', 7, 6))  
