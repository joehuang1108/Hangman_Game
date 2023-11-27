import random

# Hangman
# guess the word game
# limited amount of tries

# Game starts: new word puzzle generated w/ details specified
# ask for letter input
# if letter input exist in word, display letter instead of _ _ _
# else: tries -= 1
# repeat until word = guessed or out of tries


word_bank = ["water", "cooler", "summer"]
word = random.choice(word_bank)
print(len(word))

