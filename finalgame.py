#intro
print ("Welcome to Hangman")
#user welcome
name = input("What's your name?")


print ("Hello, " + name, "Let's begin!")

from random import choice
from time import sleep
#Start of games
class Hangman:
  
    _HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """)

    _WORDS = ("YEARUP","LCACHEIVE","PYTHON","HTML","FINAL PROGRAMMING","MELODY","QUALITYASSURENCE","HANGMAN","LCRESILIENT","LCIGNITE")
    _POSITIVE_SAYINGS = ("Okay getting somewhere", "Good job!", "WOW!!")
#(self)binds the attributes with the given arguments
    def __init__(self):
        #Python constructor for this class
        self._word = choice(self._WORDS)
        self._so_far = "-" * len(self._word)
        self._used = []
        self._wrong_answers = 0

    def play(self):
        #This is the main driver of the game ==>Plays the game
        self._reset_game()
        self._start_game()

        # The amount of incorrect answers greater than the length of HANGMAN
        # overflow error when printing current progress.
        while self._wrong_answers < len(self._HANGMAN) and self._so_far != self._word:
            self._print_current_progress()
            guess = self._user_guess()
            self._check_answer(guess)

        self._print_result()
        self._play_again()

    # ---------------------------------
    # "Private" methods which means that it can't access or call that method outside the class to which the method belongs to

    def _check_answer(self, guess):
        #Checks the user's guess is correct==>User's guess
        if guess in self._word:
            print(choice(self._POSITIVE_SAYINGS), "...Updating word ...")

            for i in range(len(self._word)):
                if guess == self._word[i]:

                    #correctly guessed letter : to the end

                    self._so_far = self._so_far[:i] + guess + self._so_far[i+1:]

        else:
            print("Sorry, Try again!!")
            self._wrong_answers += 1

    def _play_again(self):
       #Asks the user if he or she would like to play again.
        #If the user wants to play again, it calls play().if not, thanks the user for playing.. thats all
       
        print("What to give it another try?")
        user_input = input("Enter (Y) for yes or (N) for no: ").upper()

        if user_input == "Y":
            self.play()

        else:
            print()
            print("Thank you for playing!")

    def _print_current_progress(self):
       #Prints the current progress of the game
        print()
        print(self._HANGMAN[self._wrong_answers])
        print("Word so far: ", self._so_far)
        print("Letters used: ", sorted(self._used))

    def _print_result(self):
        #Prints the score (win or lose)
        sleep(1)
        print()
        print("Loading score...")
        sleep(1)
        print()
        if self._wrong_answers == len(self._HANGMAN):
            print("Oops you've lost! Maybe next time")
        else:
            print("Whoop whoop your a WINNER! Congratulations!")

    def _reset_game(self):
        #Resets the game==> it calls the constructor
        self.__init__()

    def _start_game(self):
      #Starts game by printing an intro & asks the user to hit the ENTER key to continue
        print()
        print("\t\tWelcome to Hangman!")
        print()
        input("Press Enter to START:")

    def _user_guess(self):
        #Asks for the user to guess a letter
        guess = input("Guess a letter: ").upper()
        sleep(1)  # Time delay
        print()

        while guess in self._used:
            print("Oops... This letter has already been used.")
            guess = input("Try another letter: ").upper()
            sleep(1)
            print()

        self._used.append(guess)

        return guess

if __name__ == '__main__':
    game = Hangman()

    game.play()