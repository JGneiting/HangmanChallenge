from Hangman.Interface import Interface


class AsciiHangman:

    def __init__(self):
        self.parts_added = 0
        self.part_order = [self.head, self.body, self.left_arm, self.right_arm, self.left_leg, self.right_leg, self.dead]

        self.display = ("  ______  \n"
                        "  |       \n"
                        "  |       \n"
                        "  |       \n"
                        "  |       \n"
                        "==========\n")

    def head(self):
        self.display = ("  ______  \n"
                        "  |    ⏺  \n"
                        "  |       \n"
                        "  |       \n"
                        "  |       \n"
                        "==========\n")

    def body(self):
        self.display = ("  ______  \n"
                        "  |    ⏺  \n"
                        "  |    |  \n"
                        "  |    |  \n"
                        "  |       \n"
                        "==========\n")

    def left_arm(self):
        self.display = ("  ______  \n"
                        "  |  \\ ⏺  \n"
                        "  |   `|  \n"
                        "  |    |  \n"
                        "  |       \n"
                        "==========\n")

    def right_arm(self):
        self.display = ("  ______  \n"
                        "  |  \\ ⏺  \n"
                        "  |   `|`-\n"
                        "  |    |  \n"
                        "  |       \n"
                        "==========\n")

    def left_leg(self):
        self.display = ("  ______  \n"
                        "  |  \\ ⏺  \n"
                        "  |   `|`-\n"
                        "  |    |  \n"
                        "  |   /   \n"
                        "==========\n")

    def right_leg(self):
        self.display = ("  ______  \n"
                        "  |  \\ ⏺  \n"
                        "  |   `|`-\n"
                        "  |    |  \n"
                        "  |   / \\ \n"
                        "==========\n")

    def dead(self):
        message = "He's gone, mate"
        self.display = ("  ______  \n"
                        "  |  \\ ⏺  \n"
                        f"  |   `|`-     {message}\n"
                        "  |    |  \n"
                        "  |   / \\ \n"
                        "==========\n")

    def draw(self):
        print(self.display)

    def next_piece(self):
        """
        Function will add the next part to the ASCII Hangman
        :return:
        """
        if self.parts_added < len(self.part_order):
            self.part_order[self.parts_added]()
            self.parts_added += 1


class CommandLine(Interface):

    def __init__(self, word_length, callback):
        super().__init__(word_length, callback)
        self.guess_number = 1
        self.letters = ["_"] * self.word_len

        self.hangman = AsciiHangman()

    def draw_welcome(self):
        print(f"Welcome to Hangman! Enter letter guesses when prompted. Guesses are case insensitive")

    def draw_game(self):
        """
        Funtion asks for the initial guess
        :return:
        """
        self.hangman.draw()
        self.draw_letters()
        self.prompt_guess()

    def draw_ending(self, game_stats):
        """
        Function will draw the ending text, and prompt the user to play again
        :param game_stats:
        :return bool: Truth of user wanting to play another game
        """
        print('\n')
        self.hangman.draw()
        self.draw_letters()
        print("That is correct!")
        print(f"You guessed the word in {game_stats.get_guess_num()} tries!")
        response = input("Would you like to play again? (y/n): ")
        response = 'y' == response.lower()
        return response

    def draw_letters(self):
        """
        Function will display the letters to the screen
        :return:
        """
        display = "Your Word: "
        for letter in self.letters:
            display += f"{letter} "
        display = display[:-1]
        print(display)

    def update_letters(self, locations, letter):
        """
        Function will update the letters at the indicated locations
        :param locations: Letter indexes to update
        :param letter: Letter to populate indexes with
        :return:
        """
        for i in locations:
            self.letters[i] = letter

    def prompt_guess(self):
        """
        Function will prompt user for a guess
        :return:
        """
        guess = input(f"Guess #{self.guess_number}: ")
        guess = guess.lower()

        # Verify the guess is a letter, and is only one character long
        if guess.isalpha() and len(guess) == 1:
            if not self.guess_letter(guess):
                # User already guessed that letter
                print(f"You have already guessed {guess}!")
                self.prompt_guess()
        else:
            print("Sorry, that is an invalid guess")
            self.prompt_guess()

    def update_stats(self, stats_obj):
        """
        Function will display game statistics
        :param stats_obj: Stats object with game stats
        :return:
        """
        # self.hangman.draw()
        print(f"Guess count: {self.guess_number}")
        print(f"Correct guesses: {len(stats_obj.correct)}")
        print(f"Incorrect guesses: {len(stats_obj.incorrect)}")
        print(f"\nIncorrect letters: {' '.join(sorted(stats_obj.incorrect))}")
        self.guess_number = stats_obj.get_guess_num()

    def update_hangman(self):
        """
        Function will add the next piece of the hangman to the hangman display
        :return:
        """
        self.hangman.next_piece()

