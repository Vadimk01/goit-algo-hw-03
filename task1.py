from datetime import datetime, date

def get_days_from_today(date_string):
    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return "Помилка: введіть дату у форматі YYYY-MM-DD"

    today = date.today()
    delta = today - given_date
    return delta.days

user_input = input("Введіть дату (YYYY-MM-DD): ")
print(get_days_from_today(user_input))
