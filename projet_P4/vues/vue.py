#!/usr/bin/env python3


class ViewMenu:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("Accueil du gestionnaire de Tournoi:")
        print()

        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
            print()

    def get_user_choice(self):
        while True:
            # afficher menu
            self._display_menu()
            # demander de faire un choix
            choice = input(">> ")
            # valider  le choix
            print(choice)
            if choice in self.menu:
                # renvoyer le choix
                return self.menu[choice]

    @staticmethod
    def display_end_message(f_name, name):
        print(f'Le joueur {f_name} {name} a été créé')

    @staticmethod
    def show_report_menu():
        print("Affichage des diiférents classements")


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
            return ViewMenu.saisie_chiffre(message)

