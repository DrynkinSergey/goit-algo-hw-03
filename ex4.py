from datetime import datetime,timedelta

users = [
    {"name": "John Doe", "birthday": "2024.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.14"},
    {"name": "Sam Smith", "birthday": "1990.03.22"},
    {"name": "Mary Jane", "birthday": "1990.04.13"},
    {"name": "Jane Dino", "birthday": "1994.02.17"}
]


def normalize_users_date(users_list, today=datetime.today()):
    """
    Функция нормализирует даты для корректной работы с разными годами рождения.

    :param users_list: Список пользователей
    :param today: Текущий день
    :return: Возвращается год пользователя приравнивая к текущему
    """
    return [{"name": user['name'], "birthday": datetime.strptime(user["birthday"], "%Y.%m.%d")
    .date()
    .replace(year=today.year)} for user in users_list]


def modified_users_date(date):
    """
    Функция хелпер для перевода поздравления на понедельник. Если день выпал на выходной
    :param date: День рождения пользователя
    :return: День поздравления
    """
    if date.weekday() in {5, 6}:
        return date + timedelta(days=7 - date.weekday())
    return date


def get_upcoming_birthdays(users_list: list) -> list:
    """
    Функция определяет список людей для поздравлений.
    Если день рождения выпадает на выходной - переносит на первый рабочий (пн)

    :param users_list: Массив пользователей
    :return: Массив пользователей для поздравлений в след 7 дней
    """
    today = datetime.today()
    normalized_users = normalize_users_date(users_list)
    delta_today_period = today.date() + timedelta(days=7)
    return[{"name": user['name'], "congratulation_date": modified_users_date(user['birthday'])}
           for user in normalized_users if user['birthday'] <= delta_today_period]


print(get_upcoming_birthdays(users))