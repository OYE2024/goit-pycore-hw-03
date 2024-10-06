"""
Функція get_upcoming_birthdays визначає кого з колег потрібно привітати.
Функція повертає список колег у кого день народження вперед на 7 днів включаючи поточний день.
Функція також враховує якщо д/р припадає на вихідний та переносить дату привітання на наступний 
робочий день.
Функція приймає список словників де кожен словник містить ключі name (ім'я користувача, рядок) та 
birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name)
та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата'.
"""

from datetime import datetime, timedelta
from calendar import weekday


users = [
    {"name": "John Doe", "birthday": "1985.10.06"},
    {"name": "Jane Smith", "birthday": "1990.10.14"}
]

# період порівняння: поточна дата (включно) + 7 днів
# отримати поточну дату (тільки дата)
# завантажити календар
# порівняти якщо дата зі списку є в періоді порівняння, та не припадає на вихідний, то вивести її в окремий список
# якщо співпадає - вивести дату привітання на наступний робочий день


def get_upcoming_birthdays(users: list) -> list:
    congrat_lst = []
    current_date = datetime.now().date()
    last_date_of_period = current_date + timedelta(days=6)
    for i in users:
        birthd_day = datetime.strptime(i["birthday"], "%Y.%m.%d").date().replace(
            year=current_date.year)
        if current_date <= birthd_day <= last_date_of_period:
            match weekday(birthd_day.year, birthd_day.month, birthd_day.day):
                case 5:
                    i["birthday"] = (
                        birthd_day + timedelta(days=2)).strftime("%Y.%m.%d")
                    congrat_lst.append(i)
                case 6:
                    i["birthday"] = (
                        birthd_day + timedelta(days=1)).strftime("%Y.%m.%d")
                    congrat_lst.append(i)
                case _:
                    i["birthday"] = birthd_day.strftime("%Y.%m.%d")
                    congrat_lst.append(i)
    return congrat_lst


print(get_upcoming_birthdays(users))
