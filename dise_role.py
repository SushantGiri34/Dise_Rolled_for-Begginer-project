import random

print("🎲 Welcome to the Dice Rolling Simulator!")

while True:
    user_input = input("\nPress Enter to roll the dice or type 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Thanks for playing! 🎉")
        break
    else:
        dice_number = random.randint(1, 6)
        print(f"🎯 You rolled a {dice_number}!")

