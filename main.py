import random
import os

DEFAULT_MIN = 0
DEFAULT_MAX = 100

min = 0
max = 0

def clear():
    # check and make call for specific operating system
    os.system('clear' if os.name == 'posix' else 'cls')

def validate_input(a) -> bool:
    try:
        int(a) + 1
        return True
    except:
        return False

def main():
    in_min = input(f"Enter Min ({DEFAULT_MIN}): ")
    if(validate_input(in_min)):
        min = int(in_min)
    else:
        min = DEFAULT_MIN

    in_max = input(f"Enter Max ({DEFAULT_MAX}): ")
    if(validate_input(in_max)):
        max = int(in_max)
    else:
        max = DEFAULT_MAX

    gen = random.randint(min, max)
    guess_count = 0
    while True:
        guess_count += 1
        guess = "blyat davai"
        while validate_input(guess) == False:
            guess = input("Guess: ")
        guess = int(guess)
        if(guess > gen):
            print(f"{guess} is bigger")
        elif(guess < gen):
            print(f"{guess} is smaller")
        if(guess == gen):
            clear()
            if(input(f"{guess} is the number!\nNumber Of Guesses: {guess_count}\nPlay again? (Y/N)").lower() == "y"):
                gen = random.randint(min, max)
                guess_count = 0
                clear()
            else:
                exit(0)

if(__name__ == "__main__"):
    main()