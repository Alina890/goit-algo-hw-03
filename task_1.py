from datetime import datetime

def get_days_from_today(date):
    user_date = input("Введіть дату: ")
    date = datetime.strptime(user_date, '%Y.%m.%d')
    current_date = datetime.today()
    date = date.replace(year=current_date.year)
    delta_date =  current_date - date 
    if delta_date.days > 0:
        print(f"{delta_date.days} днів")
    else:
        print(f"{delta_date.days} днів")

    return int(delta_date.days)
