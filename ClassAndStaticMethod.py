class Person():
    species = "Humans in this one"

    @classmethod
    def getSpecies(cls):
        print(cls.species)

    @staticmethod
    def age(age):
        if age<18:
            print("GET LOST!")
    
p = Person()
Person.getSpecies()
p.age(9)