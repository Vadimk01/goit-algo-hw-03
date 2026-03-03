import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка валідності параметрів
    if (
        min_num < 1 or
        max_num > 1000 or
        min_num > max_num or
        quantity < 1 or
        quantity > (max_num - min_num + 1)
    ):
        return []

    # Генерація унікальних чисел (включаючи max)
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    return sorted(numbers)

print(get_numbers_ticket(
    int(input("Введіть мінімальне число: ")),
    int(input("Введіть максимальне число: ")),
    int(input("Введіть к-ть: "))
))