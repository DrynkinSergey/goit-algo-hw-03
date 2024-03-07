from random import sample, randint


def get_numbers_ticket(*, min_value: int, max_value: int, quantity: int) -> list:
    """
    :param min_value: 1
    :param max_value: 1000
    :param quantity: max_value - min_value >= quantity
    :return: list[int]
    """
    if min_value < 1 or max_value > 1000:
        return []

    try:
        my_list = sample(range(min_value, max_value + 1), quantity)
        return sorted(my_list)

    except ValueError:
        print('Quantity must be less than difference between min and max')


print(get_numbers_ticket(quantity=17, min_value=33, max_value=66))



