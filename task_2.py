import random


def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    numbers_tickets = random.randrange(1,1000)
    for numbers in lottery_numbers: 
        if len(lottery_numbers) == quantity and min >= 1 and max <= 1000:
            lottery_numbers.append(numbers_tickets)
            continue
        else:
            lottery_numbers = []
    return 
    #while len(lottery_numbers) == quantity:
        #numbers_tickets = random.randrange(1,1000)
        #lottery_numbers.append(numbers_tickets)
        #continue
    #return (lottery_numbers)

min = 1
max = 1000
quantity = random.randint(1,1000)
print (get_numbers_ticket(min, max, quantity))