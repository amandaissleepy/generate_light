import random
from socket import if_nameindex

from termcolor import colored

from noise import pnoise2

def generate_land(rows=10, cols=10, noise_level=10):
    data = ["0", ".", "p", "u", "-", "+", "%", "o", " "]
    seed = random.randint(0, 100)
    land = ""
    print(f"Generate a landscape which is {cols} by {rows}")
    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += "\n"
            
    print("Finished generating landscape")
    return land

def ask_for_number(question) :
    tries = 0

    while tries < 3:
        answer = input(colored(question + "\n", "green"))

        if answer == "quit":
            quit()

        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Please input a number", "yellow"))
            tries += 1

    print (colored("Too many attempts have been made", "red"))       
    quit()
    

if __name__=="__main__":
    cols = ask_for_number("how many cols")
    rows = ask_for_number("how many rows")

    output = generate_land(cols, rows)

    print(output)
