"""
get_numbers_ticket(min, max, quantity) - повертає відсортований список випадкового набору унікальних
чисел в межах заданих параметрів.
Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
"""

from random import sample


def get_numbers_ticket(min, max, quantity) -> list:
    if min < 1 or max > 1000 or 0 < quantity > 1000:
        return []
    else:
        # max+1 тому що діапазон формує діапазон чисел не включаючи максимальне значення.
        return sorted(sample(range(min, max+1), quantity))


print(get_numbers_ticket(10, 300, 6))
