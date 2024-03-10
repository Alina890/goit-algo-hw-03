import random

min = 1
max = 1000
quantity = random.randint(1,1000)
def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    while len(lottery_numbers) == quantity:
        numbers_tickets = random.randrange(1,1000)
        lottery_numbers.append(numbers_tickets)
        return (lottery_numbers)