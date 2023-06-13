import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper
@measure_execution_time
def example_function_1():
    time.sleep(2)

@measure_execution_time
def example_function_2():
    time.sleep(3)

example_function_1()
example_function_2()