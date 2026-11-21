import random
import string
from collections import Counter
from pathlib import Path


# NUMBER GUESSING GAME

def number_guessing_game():

    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:

        try:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess == secret_number:

            score = (max_attempts - attempts + 1) * 10

            print("\nCongratulations! You guessed correctly.")
            print("Attempts:", attempts)
            print("Your Score:", score)
            return

        elif guess < secret_number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

    print("\nGame Over!")
    print("The correct number was:", secret_number)


# WORD COUNTER

def word_counter():

    print("\n===== WORD COUNTER =====")

    file_path = Path(__file__).parent / "sample.txt"

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()

        total_words = len(words)

        frequency = Counter(words)

        print("\nTotal Words:", total_words)

        print("\nWord Frequency:")

        for word, count in frequency.most_common():
            print(word, ":", count)

        print("\nWord Counter completed successfully!")

    except FileNotFoundError:

        print("Error: sample.txt file not found!")
        print("Please create sample.txt in the project folder.")

    except Exception as e:

        print("An error occurred:", e)


# MAIN MENU

def main():

    while True:

        print("\n================================")
        print("       PYTHON PROJECT 02")
        print("================================")

        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            number_guessing_game()

        elif choice == "2":

            word_counter()

        elif choice == "3":

            print("\nThank you for using the program!")
            break

        else:

            print("\nInvalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()