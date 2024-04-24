from generate import generate_random_number
from result import compute_result, check_result
from file import read_write_highscore_file
from user_input import get_user_input_number, get_user_name

#########################################################

user_name = get_user_name("Wie ist dein Name?")
num_problems = get_user_input_number("Wieviele Aufgaben sollen gelöst werden?")

num_operands = 0

while num_operands < 2:
    num_operands = get_user_input_number(
        "Wieviele Operanden sollen die Aufgaben haben?"
    )
    if num_operands < 2:
        print("Die Zahl der Operanden muss größer 1 sein.")
    else:
        break

num_correct = 0

for anzahl in range(num_problems):
    operator = "X"
    operators = ("+", "-", "*", "//")

    # operands = []
    # for _ in range(num_operands):
    #     operands.append(generate_random_number(1, 10))

    operands = [generate_random_number(1, 10) for _ in range(num_operands)]

    while operator not in operators:
        operator = input("Welchen Operator soll die Aufgabe haben? +, -, *, //:")
        if operator not in operators:
            print(f"{operator} ist kein gültiger Operator!")

    # str_operands = []
    # for operand in operands:
    #     str_operands.append(str(operand))
    # problem_str = f" {operator} ".join(str_operands)

    problem_str = f" {operator} ".join([str(operand) for operand in operands])

    print(f"Die Aufgabe: {problem_str}")

    user_result = get_user_input_number("Bitte Lösungsvorschlag eingeben.")

    result = compute_result(operands, operator)
    is_right = check_result(result, user_result)

    if is_right:
        num_correct += 1

print(f"Aufgaben richtig gelöst: {num_correct}")

highscore_info = {"user_name": user_name, "highscore": num_correct}

# read_write_highscore_file("highscore.txt", num_correct)
read_write_highscore_file("highscore.json", highscore_info)
