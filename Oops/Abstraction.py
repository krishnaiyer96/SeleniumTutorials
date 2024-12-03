# Abstraction means hiding the unnecessary implementations from the user and showing to users only what is required and can be used .
# example is a print() method is python which we use to print text but we do not see how the print method is implemented.




class Abstraction:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_eligibility(self):
        if self.age >= 18:
            details = f"The person with name {self.name} and age {self.age} is eligible to vote"
            return details
        else:
            details = f"The person with name {self.name} and age {self.age} is not eligible to vote"
            return details

voting = Abstraction("krishna Iyer" , 28)
voting1 = Abstraction("Bharati", 27)
voting2 = Abstraction("Mani", 17)

print(voting2.check_eligibility())
print(voting1.check_eligibility())
print(voting.check_eligibility())











