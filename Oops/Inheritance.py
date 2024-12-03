class Inheritance:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        det = f'The name of the person is {self.name} and the age is {self.age} eligible to vote - : '
        return det


class Voting(Inheritance):
    def __init__(self, name, age, iseligible = False):
        self.iseligible = iseligible

        Inheritance.__init__(self, name, age)

    def is_eligible(self):
        if self.age >= 18:
            self.iseligible = True
            return self.details() + str(self.iseligible)
        else:
            return self.details() + str(self.iseligible)


vote = Voting("Krishna Iyer",0 )
print(vote.is_eligible())
