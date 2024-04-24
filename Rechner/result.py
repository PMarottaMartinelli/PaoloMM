def compute_result(operands, operator):
    num_result = operands[0]
    if operator == "+":
        for operand in operands[1:]:
            num_result += operand
    elif operator == "-":
        for operand in operands[1:]:
            num_result -= operand
    elif operator == "*":
        for operand in operands[1:]:
            num_result *= operand
    else:
        for operand in operands[1:]:
            num_result //= operand

    return num_result


def check_result(num_result, user_input):
    print("Ihre Eingabe:", user_input)
    print("Das Ergebnis:", num_result)

    if user_input == num_result:
        print("Richtig!")
        return True
    else:
        print("Falsch!")
        return False
