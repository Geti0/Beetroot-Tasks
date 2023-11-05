# Task 1
def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{key}={value!r}" for key, value in kwargs.items()])
        arguments = ', '.join(filter(None, [arg_str, kwargs_str]))

        print(f"{func.__name__} called with {arguments}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(2, 3, 4)


# Task 2

def stop_words(stop_words_list):
    def decorator(func):
        def wrapper(name):
            result = func(name)
            for word in stop_words_list:
                result = result.replace(word, '*')
            return result

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


# Task 3

def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Argument type is not {type_.__name__}.")
                return False
            if len(arg) > max_length:
                print(f"Argument length exceeds {max_length}.")
                return False
            for symbol in contains:
                if symbol not in arg:
                    print(f"Argument does not contain '{symbol}'.")
                    return False
            return func(arg)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

result1 = create_slogan('johndoe05@gmail.com')
result2 = create_slogan('S@SH05')

if result1 is False:
    print("Validation failed for 'johndoe05@gmail.com'")
else:
    print(result1)

if result2 is False:
    print("Validation failed for 'S@SH05'")
else:
    print(result2)
