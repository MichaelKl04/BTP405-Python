#Timer Decorator: Write a decorator function called timer that calculates the time taken for a function to execute and prints the duration. 
#It should be able to decorate any function and print the time taken for execution.

import time

def time_Decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        print('Starting Time:', start_time)
        print("Total Time Taken: %s seconds" % (time.time() - start_time))
    return wrapper

@time_Decorator
def loop():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)


loop()