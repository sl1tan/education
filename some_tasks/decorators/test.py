import time

import requests


def wrapper(func):
    def my_print(function):
        print(f"Function - {func}")

    return my_print(func)


def decorator(function):
    def wrapper():
        print(f'catch - {function}')
        function()

    return wrapper


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'TOTAL TIME: {end - start}')

    return wrapper


def timer2(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'TOTAL TIME: {end - start}')
        return result

    return _wrapper


def benchmark(iters):
    def new_timer(func):
        def _wrapper(*args, **kwargs):
            total = 0
            result = 0
            for x in range(iters):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total += end - start
            print(f'AVG TIME: {total / iters}')
            return result

        return _wrapper

    return new_timer


@benchmark(iters=5)
def hi_google():
    response = requests.get('https://google.com')
    return response.status_code == 200


@timer2
@decorator
def test():
    print('This is test func')


def process_list(list_):
    def _decorator(function):
        return function(list_)

    return _decorator


unprocessed_list = [0, 1, 2, 3]
special_var = "don't touch me please"


@process_list(unprocessed_list)
def processed_list(items):
    special_var = 1
    return [item for item in items if item > special_var]


print(processed_list, special_var)

# l = wrapper
#
# l(print)
#
# print(type(wrapper))

# test()
# print(hi_google())
