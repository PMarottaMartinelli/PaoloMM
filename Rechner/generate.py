import random

random.seed()


def generate_random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)
