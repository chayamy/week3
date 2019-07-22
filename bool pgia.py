import random

secret_number = []


def rand():
    while len(secret_number) < 4:
        num_to_add = random.randint(1, 9)
        if num_to_add not in secret_number:
            secret_number.append(num_to_add)
    return secret_number
    print(secret_number)


def read(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 999 and num < 10000:
                return num
        except ValueError:
            pass


def check_bool_pgia(secret_number, play_number):
    bool = 0
    pgia = 0
    for i in range(0, len(secret_number)):
        if secret_number[i] == play_number[i]:
            bool += 1
        elif secret_number[i] in play_number:
            pgia += 1
    return (bool, pgia)


def main():
    bools = 0
    game = 0
    while bools < 4 and game < 20:
        pl_number = read(f"it's try {game+1}: enter your choose ")
        secret_number = rand()
        play_number = [pl_number//1000, pl_number//100 % 10, pl_number % 100//10, pl_number % 10]
        bools, pgia = check_bool_pgia(secret_number, play_number)
        print(f"{bools} bools and {pgia} pgia")
        if bools == 4:
            print("you are a champion!!!!!!")
        elif game >= 20:
            print("game over :( :( try again :::))")
        game += 1


main()
