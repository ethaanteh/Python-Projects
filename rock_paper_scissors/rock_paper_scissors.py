from random import randint 
def main():
    player_score = 0
    machine_score = 0
    game_rounds = 0
    while player_score <5 and machine_score <5:
        game_rounds += 1
        print()
        print(f"Round {game_rounds}")
        print(f"Player score = {player_score} Machine score = {machine_score}")
        player_ans = player_choice()
        machine_ans = machine_choice()
        outcome = compare_choice(player_ans, machine_ans)
        if outcome == "0":
            player_score += 1 
        if outcome == "1":
            machine_score += 1
    output_winner(player_score, machine_score, game_rounds)

def player_choice():
    valid_inputs = [
        "r",
        "p",
        "s",
        ]
    while True:
        choice = input("Enter your choice rock(r), paper(p), scissors(s): ").lower()
        if choice in valid_inputs:
            return choice
        else:
            print("Thats not an option, try again")
def machine_choice():
    choice = randint(1,3)
    if choice == 1:
        return "r"
    elif choice == 2:
        return "p"
    elif choice == 3:
        return "s"
def compare_choice(player_ans, machine_ans):
    outcome = ""
    different_outcomes = {
        "r":"s",
        "s":"p",
        "p":"r",
    }
    if player_ans == "r":
        player_pick = "rock"
    elif player_ans == "p":
        player_pick = "paper"
    elif player_ans == "s":
        player_pick = "scissors"
    if machine_ans == "r":
        machine_pick = "rock"
    elif machine_ans == "p":
        machine_pick = "paper"
    elif machine_ans == "s":
        machine_pick = "scissors"
    if different_outcomes[player_ans] == machine_ans:
        print("You win!")
        print(f"You picked {player_pick} the machine picked {machine_pick}")
        outcome = "0"
    elif different_outcomes[machine_ans] == player_ans:
        print("You lose!")
        print(f"You picked {player_pick} the machine picked {machine_pick}")
        outcome = "1"
    else:
        print("Draw!")
        print(f"You picked {player_pick} the machine picked {machine_pick}")
        outcome = "2"
    return outcome
def output_winner(player_score, machine_score, game_rounds): 
    if player_score == 5:
        print(f"You won in {game_rounds} rounds with the scores: player:{player_score} machine:{machine_score}")
    elif machine_score == 5:
        print(f"You lost in {game_rounds} rounds with the scores: player:{player_score} machine:{machine_score}")
    choice = input("Do you want to play again(y/n)?: ").lower()
    if choice == "y":
        if __name__ == "__main()__":
            main()
    elif choice == "n":
        pass
if __name__ == "__main__":
    main()