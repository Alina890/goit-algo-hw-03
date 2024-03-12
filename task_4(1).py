from datetime import datetime, timedelta

users = [
    {"name": "Alison", "birthday": "1994.08.06"},
    {"name": "Deniel", "birthday": "1990.02.12"},
    {"name": "Barbara", "birthday": "1989.04.23"},
    {"name": "Semuel", "birthday": "1996.11.03"},
    {"name": "Elisabeth", "birthday": "1999.06.05"}
]


def get_uncoming_birthdays():
    days = 7
    current_date = datetime.today().date()
    birthday_days = datetime.strptime(users["birthday"], "%Y.%m.%d").date()
    uncoming_birthdays = []
    for user in users:
        birthday_this_year = user["birthday"].replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
            if 0 <= (birthday_this_year - current_date).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = find_next_weekday(birthday_this_year, 0)
                congratulation_date_string = birthday_this_year.strftime("%Y,%m,%d")
                uncoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_string})
                print (uncoming_birthdays)
    return get_uncoming_birthdays()