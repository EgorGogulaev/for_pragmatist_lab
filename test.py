import random
from itertools import product

# With AI
def calculate_expression(expression):
    return eval(expression)

def generate_expressions(numbers, operators):
    for ops in product(operators, repeat=len(numbers)-1):
        yield ''.join([str(num) + op for num, op in zip(numbers, ops)] + [str(numbers[-1])])

# My solution
def get_all_variations(operators: list[str:], numbers: list[int:]) -> None:
    variations = []
    while True:
        variation = "".join([str(num) + random.choice(operators) if num else str(num) for num in numbers])

        if eval(variation) == 200 and variation not in variations:
            variations.append(variation)
            print(variations)

if __name__ == '__main__':
    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    operators = ['+', '-', '']

    # with AI
    for expression in generate_expressions(numbers, operators):
        if calculate_expression(expression) == 200:
            print(expression)

    # My solution
    get_all_variations(operators=operators, numbers=numbers)
