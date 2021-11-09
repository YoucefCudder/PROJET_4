#!/usr/bin/python3
# coding: utf8
from ..vues.vue_tournament import TournamentView


class ViewMenu:
    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print("Accueil du gestionnaire de Tournoi:")
        print()

        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
            print()

    def get_user_choice(self):
        while True:
            # afficher menu
            self.display_menu()
            # demander de faire un choix
            choice = input(">> ")
            # valider  le choix
            print(choice)
            if choice in self.menu:
                # renvoyer le choix
                return self.menu[choice]


class UsefulView:
    @staticmethod
    def display_end_message(f_name, name):
        print(f"Le joueur {f_name} {name} a été créé")

    @staticmethod
    def show_report_menu():
        print("\n Affichage des diiférents classements \n")
        print("1: Liste de tous les joueurs par ordre alphabétique")
        print("2: Liste de tous les joueurs par classement")
        print("3: Liste de tous les tournois")
        print("4: Retour au menu principal")

    @staticmethod
    def input_int(message):

        try:
            return int(input(message))
        except ValueError:
            print("attention ce n'est pas un chiffre ")
            return UsefulView.input_int(message)

    @staticmethod
    def time_control_options():
        print("\n Timing de la partie :")
        print("1 - Bullet")
        print("2 - Blitz")
        print("3 - Rapid")
        print("\n[back] Retour au menu principal")

    @staticmethod
    def input_prompt():
        print("\nType [option] and press Enter : ", end="")

    @staticmethod
    def input_error():
        print("\nInput error, veuillez entrer une option valide.")

    @staticmethod
    def confirmation_input():
        print("Confirmez vous les infromations saisies ? "
              "[Y] pour oui /  [N] pour non ")
        print(TournamentView.create_tournament())
        user_input = input()
        if user_input == "Y":
            pass
        elif user_input == "N":
            return TournamentView.create_tournament()

