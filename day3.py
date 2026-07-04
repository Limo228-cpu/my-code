import random
name = input("Представьтесь для начала игры\n")
secret = random.randint(1, 1000)
tries = 0
print(f"Привет {name} загадал число от 1 до 1000, попробуешь угадать?")
while True:
    guess = int(input("Назови предполагаемое число"))
    tries += 1
    if guess < secret:
        print("Почти угадал, попробуй число побольше\n")
    elif guess > secret:
        print("Переборщил немного, попробуй число поменьше")
    else:
        print(f"Молодец, {name}, ты угадал! Для этого тебе понадобилось {tries} попыток\n")
        break