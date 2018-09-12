# MSP
# Molly and Alex

word = input("Player 1: What's the word?")
guess = 0
print ("\n" * 50)

letter = input("Player 2: Guess a letter")

##if letter in word:
##    print("nice")
##else:
##    print("nope")
if guess < 10:
    
    for let in word:
        if let == letter:
            print(letter)
        else:
            print("_")
            
    guess += 1
    #print(guess)
    print("Guess again!")
else:
    print("no more guesses")
