import random

item_list = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your move (Rock, Paper, Scissors): ").capitalize()
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chose the same: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Wins")
    else:
        print("Rock smashes Scissors = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissors":
        print("Scissors cut Paper = Computer Wins")
    else:
        print("Paper covers Rock = You Win")

elif user_choice == "Scissors":
    if comp_choice == "Rock":
        print("Rock smashes Scissors = Computer Wins")
    else:
        print("Scissors cut Paper = You Win")

else:
    print("Invalid input! Please choose Rock, Paper, or Scissors.")
