class Meta(type):
    def __new__(cls, name, bases, attrs):
        if "save" not in attrs:
            raise TypeError("Class must implement save()")
        print(f"Classs {name} is created")
        return super().__new__(cls, name, bases, attrs)


class Employee(metaclass=Meta):
    #def save():
    pass
    
###########################
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(dct)
        if "save" not in dct:
            raise TypeError("Class must implement save()")
        print(f"Classs {name} is created")
        return super().__new__(cls, name, bases, dct)


class Employee(metaclass=Meta):
    def save():
        pass