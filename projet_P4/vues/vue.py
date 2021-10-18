#!/usr/bin/python3
# coding: utf8

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
        print(f'Le joueur {f_name} {name} a été créé')

    @staticmethod
    def show_report_menu():
        print("\n Affichage des diiférents classements \n")
        print("1: Liste de tous les joueurs par ordre alphabétique")
        print("2: Liste de tous les joueurs par classement")
        print("3: Liste de tous les tournois")
        print("4: Retour au menu principal")

    @staticmethod
    def saisie_chiffre(message):

        try:
            return int(input(message))
        except ValueError:
            print("attention ce n'est pas un chiffre ")
            return UsefulView.saisie_chiffre(message)

    @staticmethod
    def input_prompt():
        print("\nType [option] and press Enter : ", end='')

    @staticmethod
    def input_error():
        print("\nInput error, please enter a valid option.")
