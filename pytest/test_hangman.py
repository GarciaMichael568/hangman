import hangman
import words

def test_valid_word():
    word = hangman.get_valid_words(words.words)
    if '-' in word or ' ' in word:
        assert False
    else:
        assert True