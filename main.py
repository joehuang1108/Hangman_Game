import random
import webbrowser
import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Hangman
# guess the word game
# limited amount of tries

# Game starts: new word puzzle generated w/ details specified
# ask for letter input
# if letter input exist in word, display letter instead of _ _ _
# else: tries -= 1
# repeat until word = guessed or out of tries

# CHECK for invalid entries
# MAKE bigger word bank


def hangman():
    word_bank = ["water", "cooler", "summer"]
    word = random.choice(word_bank)
    print("_" * len(word))
    valid_letters = "abcdefghijklmnopqrstuvwxyz"

    guess_made = ""
    chances = 5
    while(chances > 0):
        main = ""
        guess = input("enter a guess: ")
        guess = guess.lower()

        while (guess not in valid_letters) or (guess in guess_made):
            guess = input("enter a guess: ")
            guess = guess.lower()

        guess_made += guess
        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main += "_"
        if main == word:
            print("win")
            break
        print(main)

        if guess not in word:
            chances -= 1
            print("chances" + str(chances))


def get_random_words():
    url = 'https://www.randomlists.com/random-words'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        words = soup.find_all('span.rand_large')
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    print(words)

hangman()
# get_random_words()
