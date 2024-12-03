# Encapsulation is a fundamental concept in OOP that combines data (attributes) and methods that work
# with that data into a single unit known as a class. This protective layer around the data
# maintains its integrity and prevents unauthorized access.

class Encapsulation:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        details = f"The person name is {self.name} and the age of the person is {self.age}"
        return details

encap = Encapsulation("Krishna Iyer", 28)
encap1 = Encapsulation("Bharati", 27)
print(encap1.details())
print(encap.details())

#here we are encapsulating all the data in to the class Encapsulation and calling the data and method when required
