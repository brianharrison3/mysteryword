import random
from typing import final


#pick mode


game_start = False
while game_start == False:
    if game_start == False:
        game_mode = input("What mode do you want to play, easy = 1, normal = 2, hard = 3 ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3":
            game_start = True

#getting random word for right game mode

    with open("words.txt") as wordstxt:
        all_words = wordstxt.readlines()
    random_word = random.choice(all_words)      
    random_word = random_word.lower()
   
    if game_mode == "1":
        while len(random_word) <= 3 or len(random_word) > 6:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()
    if game_mode == "2":
        while len(random_word) <= 5 or len(random_word) > 8:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()
    if game_mode == "3":
        while len(random_word) <= 7:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()

#random_word 


guess_made = ''
correct_letters = []
whole_word = len(random_word) - 1
guesses_left = 8
print("The word has" , whole_word , "letters")
# valid guesses
valid = ["a","b", "c", "d","e" ,"f" ,"g" ,"h" ,"i" ,"j" , "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]  
while game_start == True:
    
    
    
    guess = input("guess a letter ")
    guess = guess.lower()
#guess input errors
    if len(guess) > 1 or guess not in valid or guess in guess_made:
        print("Error, one letter only or chacter entered is not a valid")
    else:
        guess_made += guess 
        print("Guesses made: ", guess_made)
        

        for letter in random_word:
            if letter in guess:
                correct_letters.append(letter)
                print("There is a", letter, "in the word")
                whole_word = whole_word - 1

      
        if guess not in random_word:
            guesses_left = guesses_left - 1
            print("WRONG, be carefull you only have", guesses_left , "wrong guesses left")
        for letter in random_word:
            if letter in guess_made:
                print(letter)
            else:
                print("-")
#stop game
        
        
        
        if guesses_left == 0:
            print("out of guesses")
            final_guess = input("Guess the word ")
            print(final_guess)
            print(random_word)
            if final_guess == random_word:
                print("Thats it!!!, Your word was,", random_word)
                game_start = False
            
            else:
                print("Wrong!!!, your word was", random_word)
                print(final_guess)
                print(random_word)
                game_start = False

    
        if len(correct_letters) == len(random_word)-1:
            print("Good job you found the word" , random_word)
            game_start = False




    
    















    








