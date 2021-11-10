def ask():
    print("calculator application. Please give me the ")

    print("1. operand (integer)")
    text = input()
    while not text.isnumeric():
        print("bad input, again")
        text = input()
    operand1 = int(text)

    print("operator (+ | - | * | /)")
    text = input()
    while text not in ['+', '-', '*', '/']:
        print("bad input, again")
        text = input()
    l_operator = text

    print("2. operand (integer)")
    text = input()
    while not text.isnumeric():
        print("bad input, again")
        text = input()
    operand2 = int(text)

    return operand1, l_operator, operand2

def calculate(operand1, l_operator, operand2):
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

op1, operator, op2 = ask()
result = calculate(op1, operator, op2)
print(f"result: {result}")
exit(0)

