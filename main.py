from Calculators.AdvancedCalculatorWithVariables.access import Access as AdvancedCalculatorAccess


def main():
    equation = input("Enter an equation: ")
    access = AdvancedCalculatorAccess()
    while True:
        try:
            if equation == "exit":
                break
            result = access.interpret(equation)
            print(f"The result is: {result}")
            equation = input("Enter an equation: ")
        except ZeroDivisionError:
            print("You cannot divide by zero or take the log with base 1.")
            access.calculator.interpreter.environment.clear()
            equation = input("Enter an equation: ")
        except ValueError:
            print("Invalid equation.")
            access.calculator.interpreter.environment.clear()
            equation = input("Enter an equation: ")

if __name__ == '__main__':
    main()
