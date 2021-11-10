


def is_numeric(text):
    return text.isnumeric()


def is_supported_operator(text):
    return text in ['+', '-', '*', '/']


def calculate(operand1, operator, operand2):
    rw =0
    if operator == '+':
            rw = operand1 + operand2
    elif operator == '-':
            rw = operand1 - operand2
    elif operator == '*':
            rw = operand1 * operand2
    elif operator == '/':
            rw = operand1 / operand2
    return rw
