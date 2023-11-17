from random import randint

import Hangman

word_list = ["Pineapples",
             "Cats",
             "Train",
             "Trumpet",
             "Houses",
             "Telephone",
             "Calculators",
             "Physics",
             "Envelope",
             "Dragon"]

# Entry point for the hangman program
if __name__ == "__main__":
    play_game = True
    while play_game:
        word = word_list[randint(0, len(word_list)-1)]
        play_game = Hangman.launch_game(word)
