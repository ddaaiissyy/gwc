# --- Define your functions below! ---

def Bot():
    start = "yes"
    print("Welcome, my name is Bot.")
    userchoice = input("Would you like to chat with me?")
    if userchoice == "yes" or userchoice == "Yes":
        print("I will ask you a series of questions.")
    if userchoice == "no":
        quit()  
        


Bot()
def act_1():
    keepchatting = "yes"
    while keepchatting == "yes":
        userchoice_act1 = input("How's it going? good or not so well?")
        if userchoice_act1 == "good":
            print("ok. Next question.")
            keepchatting = "no"
        if userchoice_act1 == "not so well":
            print("I have no response since robots don't have emotions.")
            print("My series of questions end here, hope to see you again.")
            keepchatting = input("Would you like to chat again?")
            if keepchatting == "no":
                quit()
act_1()
def act_2():
    keepchatting = "yes"
    while keepchatting == "yes":
        userchoice_act2 = input("Do you prefer dogs or cats?")
        if userchoice_act2 == "dogs":
            print("cool. next question")
            quit()
        if userchoice_act2 == "cats":
            print("You see I don't like cats...")
            print("My series of questions end here, hope to see you again.")
            keepchatting = input("Would you like to chat again?")
            if keepchatting == "no":
                quit()
act_2()









