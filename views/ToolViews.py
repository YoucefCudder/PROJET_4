#!/usr/bin/python3
# coding: utf8
import datetime
import re


class InputCheckView:
    """
    class useful to check every type of data incorporated in the software by the user.
    """

    def __init__(self):
        """ """
        self.error_handler = ErrorHandlerView()

    def check_string(self, message):
        """method useful to check a string registered via inputs"""
        while True:
            user_input = input(message)
            if re.search("^[\\w ]{3,}$", user_input):
                return user_input
            self.error_handler.display_error("Mauvais format")

    def check_int(self, message):
        """method useful to check the integer in the input"""
        while True:
            try:
                return int(input(message))
            except ValueError:
                self.error_handler.display_error("Mauvais format")

    def check_sex(self, message):
        """method useful to check if the gender is correctly determined in the user input."""
        while True:
            user_input = input(message)
            if user_input == "M" or user_input == "F":
                return user_input
            self.error_handler.display_error("Mauvais format (M ou F)")

    def input_in_array_of_int(self, message, array):
        """method useful to determine if the input of an integer is contained in an array."""
        while True:
            user_input = int(input(message))
            if user_input in array:
                return user_input
            self.error_handler.display_error("numéro inconnu")

    def time_option(self):
        """method useful to choose the timing option of the chess tournament"""
        while True:
            print("Timing de la partie:")
            print("1: Bullet")
            print("2: Blitz")
            print("3: Rapid")
            user_input = input("Votre choix: ")
            if user_input == "1":
                return "Bullet"
            elif user_input == "2":
                return "Blitz"
            elif user_input == "3":
                return "Rapid"
            else:
                self.error_handler.display_error("mauvais format")

    def result_option(self):
        """method useful to choose correctly the score of a player"""
        while True:
            user_input = input("Quel est le résultat ? (1, 2 ou D en cas d'égalité)")
            if user_input == "1" or user_input == "2" or user_input == "D":
                return user_input
            else:
                self.error_handler.display_error("mauvais format")

    def check_date(self, message):
        """method useful to check the format of a date"""
        while True:
            try:
                input_date = input(message)
                day, month, year = input_date.split("/")
                datetime.datetime(int(year), int(month), int(day))
                return input_date
            except ValueError:
                self.error_handler.display_error("mauvais format")


class ReportView:
    """class related to the reports menu"""

    @classmethod
    def show_options(cls):
        """method useful to show the options in order to sort the players"""
        print(
            "\n1 - Afficher les joueurs triés par nom \n",
            "2 - Afficher les joueurs triés par classement \n",
        )

    @classmethod
    def show_options_for_tournament(cls):
        """method useful to show the options and select a type of report for a tournament."""
        print(
            "\n1 - Afficher les tournois \n",
            "2 - Afficher les rounds du tournoi selectionné \n"
            "3 - Afficher les matches du tournoi selectionné \n",
        )


class ErrorHandlerView:
    """class useful to manage errors"""

    @classmethod
    def display_error(cls, error):
        """method useful when an error occurs."""
        print(f"\033[31mErreur\033[00m: {error}")
