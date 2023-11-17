class Stats:

    def __init__(self):
        self.correct = []
        self.incorrect = []

    def get_guess_num(self):
        """
        Function will return the current guess number of the game
        :return int: Guess number
        """
        return len(self.correct) + len(self.incorrect) + 1


class Hangman:
    """
    This class will manage the game of hangman.
    """

    def __init__(self, word, interface):
        """
        Initialize the game with a word to guess.
        :param word: The word to guess.
        :param interface: Interface Class
        """
        self.word = word.lower()  # type: str
        self.word_copy = word.lower()
        self.guesses = []
        self.stats = Stats()
        self.interface = interface(len(self.word), self.guess_letter)

    def run_game(self):
        """
        Function will start the game with the given interface
        :return bool: Boolean indicating if the user wants to play again
        """
        self.interface.draw_welcome()
        while self.word_copy != "":
            self.interface.draw_game()
        return self.interface.draw_ending(self.stats)

    def guess_letter(self, letter):
        """
        This function will guess a letter
        :param letter: Letter to guess
        :return bool: True if guess is valid, false otherwise
        """
        if letter in self.guesses:
            return False
        self.guesses.append(letter)
        locations = []

        # Add indexes of letter in word to locations
        for i, char in enumerate(self.word):
            if char == letter:
                locations.append(i)
        locations = tuple(locations)
        self.word_copy = self.word_copy.replace(letter, "")

        # Update game statistics
        if len(locations) > 0:
            # Guess was a correct guess
            self.stats.correct.append(letter)
            self.interface.update_letters(locations, letter)
        else:
            # Guess was an incorrect guess
            self.stats.incorrect.append(letter)
            self.interface.update_hangman()

        # Update game statistics on the interface
        self.interface.update_stats(self.stats)

        return True
