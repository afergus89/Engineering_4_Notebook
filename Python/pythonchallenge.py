##MSP
##Molly and Alex

word = input("Player 1: What's the word?")
print ("\n" * 50)
blanks = [] 
for i in word:
    blanks.append('_')
print(blanks)

letter = input("Player 2: Guess a letter")
tries = 0
playerguess = None
guessedletters = []

myArray = [
    "---|  ",
    "   0  ",
    "   |  ",
    "  \   ",
    "    / ",
    "   |  ",
    "  /   ",
    "   \  " ]
while tries < 10:
    guessedletters.append(letter)
    if letter not in word:
        tries +=1
        ##print("_") 
    else:
        print("correct!")
        
        blanks[3] = letter
        print(blanks)

    if "_" not in blanks:
        print("You won!")
        break
    letter = input("Guess again!")
    
    ##for let in word:
        ##if let == letter:
            ##print(letter)
        ##else:
            ##print("_")
            
if tries == 10:
    print("You lost :(")
    print("Word was: " + word) 


    
