import random, time
import os

score = 0

os.system('cls' if os.name == 'nt' else 'clear')

def game_loop():

    global score

    print("Crossy Road🃏")
    menu = input("""S(Start)▶️
Q(Quit)❌""")

    if menu == "S":
        while True:
            car = random.randint(0, 1)
            print("Score: ", score)
            move = input("Move?Y/N: ")

            if car == 1:
                print("You crashed!")
                again = input("Again?N/Y: ")
                if again == "Y":
                    continue

                elif again == "N":
                    exit()

            if move == "Y":
                print("move")
                score += 1
                continue

            elif move == "N":
                print("Same...")
                continue

    elif menu == "Q":
        exit()

game_loop()