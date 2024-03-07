from datetime import datetime


def get_days_from_today(*, date: str) -> int:
    """
    :param date: Format must be "YYYY-MM-DD". Example: "2023-01-01"
    :return: int, days from today
    """

    now = datetime.today().date()
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d').date()
        return (now-user_date).days
    except ValueError:
        print('Date is not correct! Format must be "YYYY-MM-DD". Example: "2023-01-01" ')


print(get_days_from_today(date='2023-03-10'))
print(get_days_from_today(date='2021-03-10'))
print(get_days_from_today(date='2022-03-10'))
print(get_days_from_today(date='2022-0310'))