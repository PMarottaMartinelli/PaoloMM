def get_user_input_number(prompt):
    """Ask user for integer input and validate input.

    Args:
        prompt (str): prompt displayed to user

    Returns:
        int: user input converted to int
    """

    while True:
        try:
            num = input(f"{prompt}: ")
            num = int(num)
        except ValueError:
            print("Keine gültige Zahl!")
        else:
            break

    return num


def get_user_name(prompt):
    """Asks user for name.

    Args:
        prompt (str): prompt displayed to user

    Returns:
        str: user input
    """
    name = input(f"{prompt}: ")
    return name
