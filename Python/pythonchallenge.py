##MSP
##Molly and Alex

word = input(str("Player 1: What's the word?"))
for i in range(0,len(word)):
        print(i)
        print(word[i])
print ("\n" * 50)
blanks = [] 
for i in word:
    blanks.append('_')
print(blanks)

#letter = input(str("Player 2: Guess a letter"))
tries = 0
guessedletters = []

myArray = [
          "                   @@@                    ",
          "                   @@@                    ",
          "                    @@@                   ",
          "                    @@@                   ",
          "            @@@@@@@@@@@@@@@@@@@           ",
          "          @@@@@@@@@@@@@@@@@@@@@@@         ",
          "        @@@@@@@@@@@@@@@@@@@@@@@@@@@       ",
          "      @@@@@@@@ @@@@@@@@@@@@@ @@@@@@@@     ",
          "    @@@@@@@@@   @@@@@@@@@@@   @@@@@@@@@   ",
          "  @@@@@@@@@@     @@@@@@@@@     @@@@@@@@@@ ",
          "  @@@@@@@@@       @@@ @@@       @@@@@@@@@ ",
          "  @@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@ ",
          "  @@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@ ",
          "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ",
          "  @@@@@@@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@ ",
          "    @@@@@@  @@ @@ @@ @@ @@ @@ @  @@@@@@   ",
          "      @@@@@                     @@@@@     ",
          "        @@@@  @@ @@ @@ @@ @@ @ @@@@       ",
          "          @@@@@@@@@@@@@@@@@@@@@@@         ",
          "            @@@@@@@@@@@@@@@@@@@           ",
          "              @@@@@@@@@@@@@@@             ",
    ]
while tries < 10:
    letter = input("Player 2, guess a letter: ")
    guessedletters.append(letter)
    if letter not in word:
        tries +=1
        ##print("_") 
    else:
        print("correct!")
    for i in range(0,len(myArray)-tries):
        print(myArray[i])
        
    i = 0
        
    for let in word:
        if let == letter:
            blanks[i] = letter
        i +=1
    print(blanks)

    if "_" not in blanks:
        print("You won! :)")
        break

    
    ##for let in word:
        ##if let == letter:
            ##blanks[i] = letter
        ##else:
            ##print("_")
            
if tries == 10:
    print("You lost :(")
    print("Word was: " + word) 


    
