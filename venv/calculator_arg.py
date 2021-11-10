import sys

import secret_logic


def print_usage_and_exit():
    print("calculator app. usage: OPERAND OPERATOR OPERAND. f.e. 3 + 4")
    exit(-1)


def process_one_row(row):
    parts = row.split()
    if len(parts.argv) != 3:
        print_usage_and_exit()
    pass


def get_input():

    for row in sys.stdin:
        process_one_row(row)

    if len(sys.argv) != 4:
        print_usage_and_exit()

    if not secret_logic.is_numeric(sys.argv[1]):
        print_usage_and_exit()
    op1 = int(sys.argv[1])

    if not secret_logic.is_supported_operator(sys.argv[2]):
        print_usage_and_exit()
    operator = sys.argv[2]

    if not secret_logic.is_numeric(sys.argv[3]):
        print_usage_and_exit()
    op2 = int(sys.argv[3])
    return op1, operator, op2

operandus1, operator, operandus2 = get_input()
result = secret_logic.calculate(operandus1, operator, operandus2)
print(f"result: {result}")
exit(0)
