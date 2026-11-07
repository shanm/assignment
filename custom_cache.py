def custom_cache(func):
    cache_store = {}
    def wrapper(n):
        # Check cache first
        if n in cache_store:
            print(f"Cache HIT for fibonacci({n})")
            return cache_store[n]
        print(f"Cache MISS for fibonacci({n})")
        
        # Call original function
        result = func(n)
        
        # Store result
        cache_store[n] = result
        return result
    return wrapper


@custom_cache
def fibonacci(n):
    print(f"Calculating fibonacci({n})")
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))
print(fibonacci(5))
print(fibonacci(3))
    