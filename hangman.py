import random
from words import words
import string
def get_valid_words(words):
    word = random.choice(words) #takes in list and chooses from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase) # letters in the alphabet
    used_letters = set() # what letters the user has guessed
    
    lives = 6
    #getting user input
    #loop until word is complete: set word_letters length is zero
    while len(word_letters) > 0:
        #letters used
        print('Lives: ', end=" ")
        for x in range(lives): 
            print ('\u2764',end=" ")
        print('\nYou have used these letters: ', ' '.join(used_letters))
        
        #what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        #Check to see if user letter is in alphabet and not in used letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #Takes away a life if wrong
        #User input letter already used
        elif user_letter in used_letters:
            print("Character already used. Please try again!")
        #User input invalid character
        else:
            print("Invalid character! Please try again!")
    #when len(word_letters == 0)
    print("Congratulations! You guessed the word: ", ' '.join(word))
if __name__ == "__main__":
    hangman() 