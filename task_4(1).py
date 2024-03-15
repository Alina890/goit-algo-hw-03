from datetime import datetime, timedelta

users = [
    {"name": "Alison", "birthday": "1994.08.06"},
    {"name": "Deniel", "birthday": "1990.03.16"},
    {"name": "Barbara", "birthday": "1989.03.17"},
    {"name": "Semuel", "birthday": "1996.11.03"},
    {"name": "Elisabeth", "birthday": "1999.06.05"}
]

def find_next_weekday(day,weekday: int):
    days_ahead = weekday - day.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return day + timedelta(days = days_ahead)

def get_prepared_users(users):
    prepared_users = []
    for user in users:
        try:
            birthday_days = datetime.strptime(users["birthday"], "%Y.%m.%d").date()
            prepared_users.append({"name": user["name"], "birthday": birthday_days})
        except ValueError:
            print(f"Некоректна дата народження для користувача {user["name"]}")
    return (prepared_users)

def get_uncoming_birthdays(prepared_users):
    days = 7
    current_date = datetime.today().date()
    uncoming_birthdays = []
    for user in prepared_users:
        birthday_days = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_days.replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
        if 0 <= (birthday_this_year - current_date).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date_string = birthday_this_year.strftime("%Y,%m,%d")
            uncoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_string})
    return (uncoming_birthdays) 

print (get_uncoming_birthdays(users))