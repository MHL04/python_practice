#guessing game
#user will guess a number between 1 and 10, the computer will generate a random number between 1 and 10, 
# if the user guess the number correctly it will print "you win" if not it will print "you lose"
#we will keep track of the number of attempts the user has made and print it at the end of the game
#we will also keep track of the number of wins and losses and print it at the end of the game

import random 

wins = 0
losses = 0
attempts = 0

print("Welcome to the Guessing Game!")

print("I have selected a number between 1 and 26. Can you guess what it is?")

computer_number = random.randint(1,26)

while True:
    while True:
        try:
        
            user_guess= int(input("Enter your guess between 1 and 26 "))
        
        except ValueError:
            print("Please enter an number between 1 to 26 :") 
            continue
            
        user_guess = (user_guess)
        attempts+=1
        if user_guess == computer_number:
            print("Good job you Guess the right number")
            wins+=1
            break
        else:
            print("You Loses")
            losses+=1
            break
        
            
        
    
        
    while True:
            
            play_more= input("Do you want to play more : YES or NO : ").strip().lower()
            if play_more in ("yes", "no"):
                break
            print("please answer yes or no : ")
            
    if play_more =="no":
                break
           
                       
print(f"Number of Attemps : {attempts}")
print(f" You Wins : {wins} times")
print(f"You Lose : {losses} times")
                    
                    
            
        
