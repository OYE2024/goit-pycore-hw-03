"""
Функція normalize_phone(phone_number) нормалізує телефонні номери до стандартного формату,
залишаючи тільки цифри та символ '+' на початку. 
Функція приймає один аргумент - список з телефонними номерами у будь-якому форматі.
Функція повертає список відкорегованих номерів телефонів у міжнародному форматі.
Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України).  
"""
# приймає рядок, повертає рядок
# видаляє зайві символи, окрім "+". Номер телефону це завжди тільки цифри та символ "+"
# додає код країни (Україна) за наступним форматом: +38
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number: list) -> list:
    normalize_phone_numbers = []
    for i in phone_number:
        sanitized_number = re.sub(r"[^0-9+]", "", i)
        if len(sanitized_number) == 10:
            normalize_phone_numbers.append('+38'+sanitized_number)
        elif len(sanitized_number) == 12:
            normalize_phone_numbers.append('+'+sanitized_number)
        else:
            normalize_phone_numbers.append(sanitized_number)
    return normalize_phone_numbers


print(normalize_phone(raw_numbers))
