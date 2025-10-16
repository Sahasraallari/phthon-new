import random
while True:
    user_action = input("Enter a choic(rock , paper , sicssors):")
    possible_actions = ["rock" , "paper" , "sicssors" , ]
    computer_action =  random.choice (possible_actions)
    print(f ," \nYou choose {user_action} , computer choose {computer_action} .\n")

if user_action == computer_action:
    print(f "Both players selected{use_action}.It is a tie!")
elif user_action == "rock":
    if computer_action == "sicssors":
        print("Rock Smashes SicssorsYou win!!!! ")
    else:
        print("Paper covers Rock You loose!!")
        elif user_action = "paper":

        if computer_action == "rock":
            print("Paper covers rock you win!!")
        else:
            print("Sicssors cut paper you loose!!")
        else:
        print("Rock smasghes you loose!!")
        play_again = input ("Play again? (y/n): ")
        if play_again !=  "y":
            break






            


    








