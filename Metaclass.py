#Metaclass Example
# Define a metaclass
class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        dct['custom_attribute'] = 'Metaclass Added This!'
        return super().__new__(cls, name, bases, dct)

# Create a class using the metaclass
class MyClass(metaclass=CustomMeta):
    def __init__(self):
        self.data = "Original Data"

if __name__ == "__main__":
    obj = MyClass()
    print(obj.custom_attribute)  # Output: Metaclass Added This!
