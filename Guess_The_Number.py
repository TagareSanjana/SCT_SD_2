import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def main():
    while True:
        play_game()
        play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
