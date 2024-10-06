"""
get_days_from_today - розраховує кількість днів між заданою датою та поточною датою, 
ігноруючи час (години, хвилини, секунди).
Враховує помилку типу даних на вході.
"""

from datetime import datetime

date = '2024-10-31'


def get_days_from_today(date) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        return (current_date - input_date).days
    except ValueError:
        return f'Error. Please, use this tamplate for date: YYYY-MM-DD'


print(get_days_from_today(date))
