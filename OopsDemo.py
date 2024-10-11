class Calculator:

    num = 100

    def __init__(self, a,b):
        self.a= a
        self.b =b

        print("Iam called automatically when object is created")
    def getData(self):

        print("im now executing as method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num




obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())

