from datetime import date

birthday = date(2027, 11, 6)  # поставь свой день рождения
days = (birthday - date.today()).days
print(f"До дня рождения осталось {days} дней")
print("День 1. Цепь началась.")
name = input("Как тебя зовут? ")
print(f"{name}, увидимся завтра. День 2 ждёт.")