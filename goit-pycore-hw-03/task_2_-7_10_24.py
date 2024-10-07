"""
get_numbers_ticket(min, max, quantity) - повертає відсортований список випадкового набору унікальних
чисел в межах заданих параметрів.
Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
"""

from random import sample


def get_numbers_ticket(min, max, quantity) -> list:
    try:
        if min < 1 or max > 1000 or max < quantity < min:
            return []
        else:
            # max+1 тому що діапазон формує діапазон чисел не включаючи максимальне значення.
            return sorted(sample(range(min, max+1), quantity))
    except ValueError:
        print(f"Error. Quantity must be bigger than {
              min} and less then {max}.")


print(get_numbers_ticket(10, 300, 292))
