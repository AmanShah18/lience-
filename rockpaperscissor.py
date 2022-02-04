import random
lis=['s','r','p']
chance=5
no_of_choice=0
computer_point=0
human_point=0

print("-------------- Rock paper scissor----------------\n\n")
name=input("Enter your name:")
print("s for scissor\np for papper\nr for rock")
while no_of_choice<chance:
    inp=input("Enter your choice:")
    ran=random.choice(lis)
    
    if inp==ran:
        print("both are tie")
    
    # if user enter s
    elif inp=="s"and ran=="p":
        human_point=human_point+1
        print(f" your guess {inp} and computer guess {ran} \n")
        print(f"{name} has win")
        print(f" computer point is {computer_point} and {name} point is {human_point} \n")
    
    elif inp=="s"and ran=="r":
        computer_point=computer_point+1
        print(f" your guess {inp} and computer guess {ran} \n")
        print(f"computer has win")
        print(f" computer point is {computer_point} and {name} point is {human_point} \n")
    # if user enter p
    elif inp=="p"and ran=="s":
        computer_point=computer_point+1
        print(f" your guess {inp} and computer guess {ran} \n")
        print(f"computer has win")
        print(f" computer point is {computer_point} and {name} point is {human_point} \n")

    elif inp=="p"and ran=="r":
        human_point=human_point+1
        print(f" your guess {inp} and computer guess{ran} \n")
        print(f"{name} has win")
        print(f" computer point is {computer_point} and {name} point is {human_point} \n")
    # if user input r 
    elif inp=="r"and ran=="s":
        human_point=human_point+1
        print(f" your guess {inp} and computer guess {ran} \n")
        print(f"{name} has win")
        print(f" computer point is {computer_point} and {name} point is {human_point}\n")

    elif inp=="r"and ran=="p":
        computer_point=computer_point+1
        print(f" your guess {inp} and computer guess {ran} \n")
        print(f"computer has win")
        print(f" computer point is {computer_point} and {name} point is {human_point}\n")
    else:
        print("you have enter wrong number")    
    
    no_of_choice=no_of_choice+1
    print(f"{chance-no_of_choice} is left out of choice   {chance} \n")
# print("\t \t\t Game Over")

if computer_point== human_point:
    print("  both are Tie")
elif computer_point>human_point:
    print(f"computer wins and {name} loose")
else:
    print(f"{name} wins computer loose")
