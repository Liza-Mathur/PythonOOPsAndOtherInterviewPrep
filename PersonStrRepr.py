class Person():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name}"
    
    def __repr__(self):
        return f"Person {{'name' : {self.name} }}"

p = Person("Liza")
print(p)
print(repr(p))