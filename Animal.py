class Animal():
    def speak(self):
        print("I speak")

class Dog(Animal):
    def speak(self):
        # super().speak()
        print("I bark")

if __name__=="__main__":
    dog = Dog()
    dog.speak()