from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        date = date.replace(year=current_date.year)
        delta_date =  current_date - date 
        if delta_date.days > 0:
            print(f"{delta_date.days} днів")
        else:
            print(f"{delta_date.days} днів")
    except ValueError:
        print("Введіть дату у форматі РРРР-ММ-ДД:")
        return 
    
date = input("Take date:")
print(get_days_from_today(date))