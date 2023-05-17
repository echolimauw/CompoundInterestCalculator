import sys

def main():

    principleFlt = float(input("Please enter your starting amount: "))
    interestRate = float(input("What is the average annual rate of return as a percentage?/n No percent symbol needed.: "))
    duration = int(input("How many years will this mature? (Full years only.): "))

    interestCalc = interestRate * 0.01
    currentValue = principleFlt

    for y in range(duration):
        currentValue = currentValue + (currentValue * interestCalc)
        currentValue = round(currentValue, 2)

    principleStr = str(principleFlt)
    yearStr = str(duration)
    finalValue = str(currentValue)

    print("Your intestment of " + principleStr + " will have a value after " + yearStr + " years")
    print("will have a value of: $" + finalValue)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
