import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000 or quantity < 1):
        return []
    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
        lottery_numbers.add(random.randint(min,max))
    return list(lottery_numbers)


min = 1
max = 1000
quantity = random.randint(1,1000)
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)