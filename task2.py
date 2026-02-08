import random

def get_numbers_ticket(min, max, quantity):
    if max < 1:
        return"число не може бути меншим ніж 1"
    if max > 1000:
        return "число не може бути більшим за 1000"

    return  sorted(random.sample(range(min, max),  quantity))


print(get_numbers_ticket(int(input("Введіть мінімальне число:")), int(input("Введіть максимальне число:")), int(input("Введіть к-ть:"))))