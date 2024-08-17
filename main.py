from ProgrammingLanguages.BasicCalculator.access import Access as BasicCalculatorAccess

def main():
    equation = input("Enter an equation: ")
    access = BasicCalculatorAccess(equation)
    result = access.calculate()
    print(f"The result is: {result}")


if __name__ == '__main__':
    main()
