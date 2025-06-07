import random

def guess_number_game():
    print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")
    
    secret_number = random.randint(1, 100)
    attempts_left = 7
    
    while attempts_left > 0:
        try:
            guess = int(input(f"Введіть ваше припущення: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue
        
        if guess < secret_number:
            print("Занадто маленьке!")
        elif guess > secret_number:
            print("Занадто велике!")
        else:
            print(f"Ви вгадали! Це число {secret_number}.")
            break
        
        attempts_left -= 1
    
    if attempts_left == 0 and guess != secret_number:
        print(f"На жаль, спроби закінчились. Загадане число було: {secret_number}")

if __name__ == "__main__":
    guess_number_game()