from Calculators.AdvancedCalculator import Access as AdvancedCalculatorAccess

def main():
    equation = input("Enter an equation: ")
    access = AdvancedCalculatorAccess(equation)
    result = access.interpret()
    print(f"The result is: {result}")


if __name__ == '__main__':
    main()
