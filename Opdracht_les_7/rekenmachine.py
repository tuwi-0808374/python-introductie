def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2


def calculate(input1, input2, operator):
    number1 = int(input1)
    number2 = int(input2)

    if operator == '+':
        print(add(number1, number2))
    elif operator == '-':
        print(subtract(number1, number2))
    elif operator == '*':
        print(multiply(number1, number2))
    elif operator == '/':
        print(divide(number1, number2))

input1 = input('Geef het eerste getal: \n')
input2 = input('Geef het tweede getal: \n')
operator = input('Geef de operator (+, -, * of /): \n')
calculate(input1, input2, operator)