start = "yes"
print("You're trying to get back home, whos's help do you want?")

while start == 'yes':
    userchoice = input("Pick your character. Type 1 for The Queen of Hearts, pick your character. Type 2 for The Mad Hatter") 
    if userchoice == 1:
        print("Wrong person... Try again")
    elif userchoice == 2:
        print("Good job! On to the next round")
        start = "no"

while start == 'yes':
    userchoice = input("pick your character. Type 1 for The White Queen or type 2 for Tweedledee and Tweedledum ")
    if userchoice == 1: 
        print()
