import random

user_wins=0
comp_wins=0

options= ["stone", "paper","scissors"]

while True:
    user_input=input("what do you chose stone/paper/scissors or q to quit").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num =  random.randint(0, 2)
    comp_pick = options[random_num]
    print("computer picked", comp_pick+".")

    if user_input == "stone" and comp_pick == "scissors":
        print("you win")
        user_wins+=1
    elif user_input == "paper" and comp_pick == "stone":
        print("you win")
        user_wins += 1
    elif user_input == "scissors" and comp_pick == "paper":
        print("you win")
        user_wins += 1
    elif user_input == comp_pick:
        print("tie")
    else:
        print("you lose")
        comp_wins+=1

print("you won", user_wins," times.")
print("the computer won", comp_wins," times.")

print("game ends")

