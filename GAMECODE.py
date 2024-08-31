import random
def guess_the_number():
    print("Welcome to the Guess the Number game!\nI'm thinking of a number between 1 and 100. Can you guess what it is?")
    print(" READY!!! SO Let's start")
    my_guess=input("ENTER UN GUESS\n")

    def convertible(x):
        try :
            int(x)
            return 1
        except ValueError:
            return 0
      
    while convertible(my_guess)==0 or not(1<= int(my_guess)<= 100) :
        my_guess=input("Entrez un nombre valide svp entre 1 et 100\n")
    
    my_guess=int(my_guess)   
    attempts=1
    max_attempts=2
    correct_number=random.randint(1,100)
    cpt=1
    while attempts < max_attempts :
        if my_guess==correct_number:
             print("CONHGRATULATIONS!!! U GUESSED RIGHT")
             break
        elif my_guess == correct_number -1 or my_guess == correct_number +1 :
            print("U RE SO NEAR TO FIND THE RIGHT NUMBER.PLEASE KEEP GOING")
        elif my_guess > correct_number +1 :
             print("The guess is too high")
        elif my_guess < correct_number-1 :
             print("The guess is too low")
        attempts+=1
        try:
            my_guess=int(input("RETENTEZ VOTRE CHANCE\n"))
            while not (1 <= my_guess <= 100):
                print("The guess must be a number between 1 and 100.")
                my_guess = int(input("Please enter a valid guess between 1 and 100:\n"))
            cpt+=1
            print(f"BE CAREFUL YOU HAVE {max_attempts-cpt} ATTEMPTS LEFT")
        except ValueError:
            print("Vous devez entrer un entier svp")
    if attempts==max_attempts and my_guess!= correct_number :
        print(f"u reached the max of attempts\n The correct number was {correct_number}")
        print("THE GAME IS OVER. BETTER LUCK NEXT TIME IN SHAA ALLAH")
play_again="yes"
while play_again.lower() =="yes"  :
    guess_the_number()
    play_again = input("Do you want to play again? (yes/no):\n").lower()
    while play_again.lower() not in ["yes","no"]:
        print("PLEASE ANSWER ONLY BY YES OR NO")   
        play_again = input("Do you want to play again? (yes/no):\n").lower()
    if play_again.lower() =="no":
        print("Thank you for playing! See you next time!")
        break

