from random import randint

import Hangman

word_list = ["Pineapple",
             "Cats",
             "Train",
             "Trumpet",
             "House",
             "Telephone",
             "Calculator",
             "Physics",
             "Envelope",
             "Dragon"]

# Entry point for the hangman program
if __name__ == "__main__":
    play_game = True
    while play_game:
        word = word_list[randint(0, len(word_list)-1)]
        play_game = Hangman.launch_game(word)
