import random


def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    for number in lottery_numbers: 
        numbers_tickets = random.randrange(min,max)
        try:
            if len(lottery_numbers) <= quantity and number >= min and number <= max:
                lottery_numbers.append(numbers_tickets)
                continue
            else:
                lottery_numbers = []
        except:
            print ("Спробуйте ще")
    return (lottery_numbers)

min = 1
max = 1000
quantity = random.randint(1,1000)
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)