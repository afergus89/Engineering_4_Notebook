##MSP
##Molly and Alex

word = input("Player 1: What's the word?")
print ("\n" * 50)
##print ("---\u2510","0","  |","  /|\ ","  |","  / \ ")
letter = input("Player 2: Guess a letter")
tries = 0
playerguess = None
guessedletters = []
blanks = [] 

if letter in word:
    blanks.append('_')
myArray = [
    "---|  ",
    "   0  ",
    "   |  ",
    "  \   ",
    "    / ",
    "   |  ",
    "  /   ",
    "   \  " ]

if tries < 10:
    guessedletters.append(letter)
    if letter not in word:
        tries +=1
        print("_") 
    else:
        print("correct!")
        print(letter)

    if "_" not in blanks:
        print("You won!")
    
    letter = input("Guess again!")
    
    ##for let in word:
        ##if let == letter:
            ##print(letter)
        ##else:
            ##print("_")
            
if tries == 10:
    print("You lost :(")
    print("Word was: " + word) 


    
