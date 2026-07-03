name = input("Как тебя зовут?\n")
age = int(input("Сколько тебе лет?\n"))
adult_year = 2026-age 
adult_year += 18 
if age >= 18:
    print(f"Проходи, {name}!")

else:
    print(f"Привет дорогой {name}, к сожалению ты еще слишком молод, вернись в {adult_year} году")