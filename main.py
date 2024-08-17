from Calculators.AdvancedCalculatorWithVariables.access import Access as AdvancedCalculatorAccess

def main():
    equation = input("Enter an equation: ")
    access = AdvancedCalculatorAccess()
    while True:
        if equation == "exit":
            break
        result = access.interpret(equation)
        print(f"The result is: {result}")
        equation = input("Enter an equation: ")


if __name__ == '__main__':
    main()
