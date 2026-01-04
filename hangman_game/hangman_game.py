import random
from .hangman_ASCII_art_and_words import hangman_stages, words

random_word = random.choice(words)
print(random_word)