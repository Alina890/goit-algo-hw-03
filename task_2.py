import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    if min >= 1 and max <=1000:
        while len(lottery_numbers) <= quantity:
            lottery_numbers.add(random.randint(min,max))
        return list(lottery_numbers)
    else:
            lottery_numbers = []
    


min = 1
max = 1000
quantity = random.randint(1,1000)
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)