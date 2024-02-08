#Memoization using Closures: Implement a memorization decorator using closures.
#The decorator should cache the results of a function for particular arguments 
#and return the cached result when the function is called with those arguments again, instead of recomputing it.

def memoize(func):
    #dictionary to store cache results
    cache = {}
    #Inner function to perfrom memoization
    def memoized_function(*args):
        #Check if the argument are already in cache
        if args in cache:
            #return the chaceh result if avail
            print("Fetching From Cache: ", args)
            return cache[args]
        else:
            print("Computing result for:", args)
            #compute the result using decorated function
            result = func(*args)
            #cache results for future use
            cache[args] = result
            #return results
            return result
        
    return memoized_function

#create decorated function which adds 2 numbers
@memoize
def add(a, b):
    return a + b

print(add(1,5))
print(add(2,6))
print(add(5,10))
print(add(1,5))
print(add(5,1))


