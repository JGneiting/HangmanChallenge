class Interface:
    """
    Interface is a stub class. Game interfaces must inherit from this class and override all functions
    """

    def __init__(self, word_length, callback):
        """
        Function will initialize the interface to work with a word of length word_length
        :param word_length: Length of the word
        :param callback: Class must call the callback when the user wants to send a guess into the game.
                        callback will have only one argument "letter"
        """
        self.word_len = word_length
        self.guess_letter = callback

    def update_letters(self, locations, letter):
        """
        Function will populate the indicated locations with the given letter
        :param locations: Tuple of locations to populate.
        :param letter: Char to populate locations with
        :return:
        """
        raise NotImplementedError

    def update_stats(self, stats_obj):
        """
        Updates game stats according to data from the stats_obj
        :param stats_obj: Stats object containing guess data
        :return:
        """
        raise NotImplementedError

    def update_hangman(self):
        """
        Function will update the hangman with the next part if not already completed
        :return:
        """
        raise NotImplementedError

    def draw_welcome(self):
        """
        Function will display a welcome screen to start the game
        :return:
        """
        raise NotImplementedError

    def draw_game(self):
        """
        Function will display the game window
        :return:
        """
        raise NotImplementedError

    def draw_ending(self, game_stats):
        """
        Function will draw the ending screen, prompting the user to play again
        :param game_stats: Stats obj
        :return bool: Boolean indicating whether to play again or not
        """
        raise NotImplementedError
