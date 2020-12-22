import random  # to choose randomly one word from the list of words

name=input("What is your name? ") 
print("Hello ", name , ",wish you a Good Luck! \n")

words=["IITGN" , "India" , "canvas" , "apple" , "karthikram" , "python" , "Programming" , "computing" , "code" , "project"]
word= random.choice(words) # function choose one word randomly from the set of words

print("Guess the characters ")
guesses= ' '

chances=10

while chances>0:
    failed=0 # counts number of times the player gets failed
    
    for char in word: # takes input of  all characters of the word one by one

        if char in guesses: # check whether the character is in the randomly choosen word
            print(char)
        else:
            print("_")

            failed+=1 # if player give incorrect character then it will increase by 1
    
    if failed==0: # player win the game if there is no character to be given,
                  #  means if he write all the characters of the randomly choosen word
        print("YOU WIN")
        print("The word is: ", word) # After player wins the game it shows the correct word
        break

    guess=input("guess a character: ") # if player gave the wrong character as the input 
                                       # then it will ask player to give another character
    guesses+=guess
    
    if guess not in word: # checks the input character given by player with the word
        chances-=1

        print("wrong") # if input doesn't match the word then 'wrong' will be given as output

        print("You have", + chances, 'more guesses') # shows how many turns are left for the player
        
        if chances==0: # if the player lost all the turns then he lost the game
            print('Sorry', name, ", You Lost")

print("\nThanks for playing, Visit again.")
                
            
