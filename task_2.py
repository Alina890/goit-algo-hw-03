import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    while len(lottery_numbers) <= quantity:
        if min >= 1 and max <= 1000:
            numbers_tickets = random.randrange(min,max)
            lottery_numbers.append(numbers_tickets)
            continue
        else:
            lottery_numbers = []
    return (lottery_numbers)


min = 1
max = 1000
quantity = random.randint(1,1000)
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)