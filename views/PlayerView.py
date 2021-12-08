#!/usr/bin/python3
# coding: utf8
from views.ToolViews import InputCheckView


class PlayerView:
    """class that handle what the user can see about everything related to the player."""

    def __init__(self):
        self.checker = InputCheckView()

    def create_player_input(self):
        """method useful to propose inputs in order to create a player according to the user"""
        print("Ajouter un nouveau joueur: ")
        print()
        print("Placez une majuscule lors de vos saisies")

        f_name = self.checker.check_string("Prénom: ").capitalize()
        name = self.checker.check_string("Nom: ").capitalize()
        gender = self.checker.check_sex("Genre (M ou F): ").capitalize()
        birthdate = self.checker.check_date("Date de naissance (DD-MM-YYYY): ")
        age = self.checker.check_int("Âge: ")
        ranking = self.checker.check_int("Classement: ")

        return {
            "f_name": f_name,
            "name": name,
            "gender": gender,
            "birthdate": birthdate,
            "age": age,
            "ranking": ranking,
        }

    def select_player(self, players):
        """method useful when its come to pick a specific player"""
        for key, player in enumerate(players):
            print(f"{key}: {player}")
        user_input = self.checker.input_in_array_of_int(
            "Votre choix: ", range(0, len(players))
        )
        return players[user_input]

    @classmethod
    def show_player(cls, p):
        """method to show  properly a player"""
        print(f"{p['name']} {p['f_name']}, Classement: {p['ranking']}")
