# MRO
class Base:
    def __init__(self):
        print("Initializing Base")

class LoggerMixin(Base):
    def __init__(self, log_level, **kwargs):
        print(f"Initializing LoggerMixin with level {log_level}")
        super().__init__(**kwargs)

class DatabaseMixin(Base):
    def __init__(self, db_url, **kwargs):
        print(f"Initializing DatabaseMixin with url {db_url}")
        super().__init__()

class App(LoggerMixin, DatabaseMixin):
    def __init__(self, log_level, db_url):
        #LoggerMixin.__init__(self, log_level=log_level, db_url=db_url)
        super().__init__(log_level=log_level, db_url=db_url)

print(App.mro())
#app = App(log_level="INFO", db_url="localhost:5432")

#####################################################

# Singleton Pattern
class Singleton:
    _instance = None
    def __new__(cls):
        #if not cls._instance:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, both are the same instance
print(id(s1), id(s2))

############################################

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def decorator(self, func):
        def wrapper(*args, **kwargs):
            print("Before function")
            result = func(*args, **kwargs)
            print("After function")
            return result
        return wrapper
        
    
singleton = Singleton()

@singleton.decorator
def greet(name):
    print(f"Hello {name}")
    
greet("John")
    



#print(s1 == s2)
#print(s1 is s2)


        

#################################################

genrator_list = (i for i in range(3))
print(next(genrator_list))
print(next(genrator_list))
print(next(genrator_list))

################################################

import sys

genrator_list = (i for i in range(1000))
arr_list = [i for i in range(1000)]

print(sys.getsizeof(arr_list))      # size of list object
print(sys.getsizeof(next(genrator_list))) # size of generator object
