import random
def get_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = ''
    while choice not in choices:
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice
def get_program_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(choice, program_choice):
    if choice == program_choice:
        return "It's a tie!"
    elif (choice == 'rock' and program_choice == 'scissors') or \
         (choice == 'scissors' and program_choice == 'paper') or \
         (choice == 'paper' and program_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def display_result(choice, program_choice, result):
    print(f"\nYou chose: {choice}")
    print(f"Computer chose: {program_choice}")
    print(result)
def play_again():
    return input("\nDo you want to play again? (yes/no): ").lower().startswith('y')
def main():
    user_score = 0
    computer_score = 0
    while True:
        choice = get_choice()
        program_choice = get_program_choice()
        result = determine_winner(choice, program_choice)
        display_result(choice, program_choice, result)       
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")        
        if not play_again():
            print("\nThank you for playing Final Scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break
if __name__ == "__main__":
    main()
