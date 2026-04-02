# Decorator 
"""
class Person:
    @property   # this is a decorator
    def show(self):
        print("This is a person class")

obj = Person()
obj.show        # this is a property decorator, it allows us to access the method as an attribute without calling it as a function.
"""

def decorate(func):
    def wrappper():
        print("Bdefore function hello")
        func()
        print("After function hello")
    return wrappper

@decorate
def hello():
    print("Hello World")

hello()