class Base:
    def __init__(self):
        print("Initializing Base")


class LoggerMixin(Base):
    def __init__(self, log_level):
        print(f"Initializing LoggerMixin with level {log_level}")
        super().__init__()


class DatabaseMixin(Base):
    def __init__(self, db_url):
        print(f"Initializing DatabaseMixin with url {db_url}")
        super().__init__()


class App(LoggerMixin, DatabaseMixin):
    def __init__(self, log_level, db_url):
        LoggerMixin.__init__(self, log_level)

#print(App.__mro__) 
print(App.mro())
#app = App(log_level="INFO", db_url="localhost:5432")

###########################################

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


        
