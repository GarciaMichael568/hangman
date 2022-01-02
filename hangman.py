import random
from words import words

def get_valid_words(words):
    word = random.choice(words) #takes in list and chooses from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word
    