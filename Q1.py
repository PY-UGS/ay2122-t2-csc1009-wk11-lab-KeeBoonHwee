
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Calculator:

    def __init__(self):
        self.clear()

    def adder(self):
        print("This adds two numbers : ")
        self.firstValue  = float(input("Please input first value : "))
        self.secondValue = float(input("Please input second value : "))
        result = self.firstValue + self.secondValue
        print(str(self.firstValue) + " + " + str(self.secondValue) + " = " + str(result))
        return result

    def subtractor(self):
        print("This subtracts two numbers : ")
        self.firstValue  = float(input("Please input first value : "))
        self.secondValue = float(input("Please input second value : "))
        result = self.firstValue - self.secondValue
        print(str(self.firstValue) + " - " + str(self.secondValue) + " = " + str(result))
        return result

    def multiplier(self):
        print("This multiplies two numbers : ")
        self.firstValue  = float(input("Please input first value : "))
        self.secondValue = float(input("Please input second value : "))
        result = self.firstValue * self.secondValue
        print(str(self.firstValue) + " x " + str(self.secondValue) + " = " + str(result))
        return result

    def divider(self):
        print("This divides two numbers : ")
        self.firstValue  = float(input("Please input first value : "))
        self.secondValue = float(input("Please input second value : "))
        if self.secondValue != 0:
            result = self.firstValue / self.secondValue
            print(str(self.firstValue) + " / " + str(self.secondValue) + " = " + str(result))
            return result

    def clear(self):
        self.firstValue = 0
        self.secondValue = 0
        print("Reset to first value to " + str(self.firstValue) + " , and second value to " + str(self.secondValue) + ".")
#-----------------------------------------------------------------------------------------------------------------------------------------------
calculator = Calculator()
calculator.adder()
calculator.subtractor()
calculator.multiplier()
calculator.divider()
calculator.clear()
#-----------------------------------------------------------------------------------------------------------------------------------------------