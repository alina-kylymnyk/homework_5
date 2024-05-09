from re import findall
from typing import Callable


def generator_numbers(text: str):
    elements = findall(r'\d+[.,]?\d+\d+', text)
    for element in elements:
        yield float(element.replace(',', '.'))


def sum_profit(text: str, func: Callable):
    total_sum = 0
    for element in func(text):
        total_sum += element
    return total_sum


input_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(input_text, generator_numbers)
print(f"Загальний дохід: {total_income}")
