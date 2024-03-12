import random

min = 1
max = 1000
quantity = random.randint(1,1000)
lottery_numbers = []
def get_numbers_ticket(min, max, quantity):
    while len(lottery_numbers) == quantity:
        numbers_tickets = random.randrange(1,1000)
        lottery_numbers.append(numbers_tickets)
        continue
    return (lottery_numbers)