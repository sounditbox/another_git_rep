import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Попробуй угадать число в диапазоне от 1 до 100 ;)")

    while True:
        try:
            guess = int(input("Ваше предположение: "))
            attempts += 1

            if guess < number_to_guess:
                print("Нет, больше!")
            elif guess > number_to_guess:
                print("Нет, меньше!")
            else:
                print(f"Молодчинка! Ты угадал загаданное число, попыток потребовалось: {attempts}.")
                break
        except ValueError:
            print("Мы тут вообще-то числа угадываем")


guess_the_number()
