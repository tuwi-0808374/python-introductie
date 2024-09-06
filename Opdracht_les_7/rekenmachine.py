def is_a_zero(number1, number2):
    if number1 == 0:
        print("eerste nummer is een 0")
    if number2 == 0:
        print("tweede nummer is een 0")

def add(number1, number2, debug = False):
    result = ""
    if debug:
        result = f"Debug: {number1} + {number2} = "
    result += str(number1 + number2)
    return result

def subtract(number1, number2, debug = False):
    if debug:
        return f"Debug: {number1} - {number2} = {number1 - number2}"
    return number1 - number2

def multiply(number1, number2, debug = False):
    if debug:
        return f"Debug: {number1} * {number2} = {number1 * number2}"
    return number1 * number2

def divide(number1, number2, debug = False):
    if debug:
        return f"Debug: {number1} / {number2} = {number1 / number2}"
    return number1 / number2


def calculate(input1, input2, operator, debug):
    number1 = int(input1)
    number2 = int(input2)

    is_a_zero(number1, number2)

    if operator == '+':
        print(add(number1, number2, debug == "y"))
    elif operator == '-':
        print(subtract(number1, number2, debug == "y"))
    elif operator == '*':
        print(multiply(number1, number2, debug == "y"))
    elif operator == '/':
        print(divide(number1, number2, debug == "y"))

input1 = input('Geef het eerste getal: \n')
input2 = input('Geef het tweede getal: \n')
operator = input('Geef de operator (+, -, * of /): \n')
debug = input('Debug? y/n: \n')
calculate(input1, input2, operator, debug)