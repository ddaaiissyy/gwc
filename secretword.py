secretword = "Basketball" 
userguess = "player"

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#SOME USEFUL VARIABLES 
guesses = [15]
maxfails = [15]
Fails = 10 
 
for Basketball in range (0,16):
    if (secretword[Basketball] == userguess): 
        userguess = input
        guesses[Basketball] = userguess 



 