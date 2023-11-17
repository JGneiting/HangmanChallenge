from Hangman import GameManager, CommandLineInterface

# Sets the interface to use with hangman game. Allows for easy integration with various interface types
interface = CommandLineInterface.CommandLine


def launch_game(word):
    """
    Will launch a game of hangman with preconfigured interface
    :param word: word to run game with
    :return:
    """
    game_obj = GameManager.Hangman(word, interface)
    return game_obj.run_game()
