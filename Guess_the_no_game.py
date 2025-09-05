import random as rd
# GUESS THE NO.
    # between 1 and 10
print(f"guess the number between 1 and 10")
def guess_number(r):
    count = 0
    while True:
        num = int(input(f"Enter a number to guess: "))
        count += 1
        if num == r:
            print(f"You guessed correctly! \n\tIn {count} guesses")
            break
        elif num < r:
            print(f"please enter a number greater than {num}")
        else:
            if (num >= 1 and num <= 10):
                print(f"please enter a number less than {num}")
            else:
                print(f"entered no is out of range")
            
r = rd.randint(1,10)
guess_number(r)
