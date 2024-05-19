import random

def roll_dice(num_sides, num_rolls):
    rolls = [random.randint(1, num_sides) for _ in range(num_rolls)]
    return rolls

def main():
    print("Welcome to the Dice Roller!")


    num_sides = int(input("Enter the number of sides on the die: "))
    num_rolls = int(input("Enter the number of times to roll the die: "))

    results = roll_dice(num_sides, num_rolls)

    print(f"Results of rolling a {num_sides}-sided die {num_rolls} times: {results}")

if __name__== "__main__":
    main()


