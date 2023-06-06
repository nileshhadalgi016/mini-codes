import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        user_input = input("Press Enter to roll the dice (or enter 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break

        dice_result = roll_dice()
        print("You rolled a", dice_result)


if __name__ == '__main__':
    main()
