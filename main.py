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
print("_" * len(word))

# this holds the display of hidden word

# this holds onto all the letters that was guessed
guess_made = ""
chances = 5
# while(chances > 0):
#     main = ""
#     guess = input("enter a guess: ")
#     guess_made += guess
#     for letter in word:
#         if letter in guess_made:
#             main = main + letter
#         else:
#             main += "_"
#     print(main)
#
#     if guess not in word:
#         chances -= 1

print("Hello")
print("World")



# summer
# sum
# __m
