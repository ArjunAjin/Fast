class Calculator:

    def add(self, a, b):
        return a + b


calc = Calculator()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calc.add(num1, num2)

print("Addition =", result)