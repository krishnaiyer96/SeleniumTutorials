class Calculation:

    def __init__(self, name, num4, num5):
        self.num4 = num4
        self.num5 = num5
        self.name = name


    @staticmethod
    def add_num(num1, num2):
        num3 = num1 + num2
        return num3
    @classmethod
    def subtract_num(cls, num4, num5):
        return cls("Krishna",num4 ,num5)


print(Calculation.add_num(2,3))
Print = Calculation.subtract_num(3,4)
print(Print.name)
print(Print.num4)
print(Print.num5)

# @staticmethods decorator is used when we do not want to create any constructor want want o make a method static that is it can be called by using class without creating any Object for the class
# @classmethod decorator is used when we want to use the class paramenter which has been declared in the constructor.
