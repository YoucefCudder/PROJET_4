#!/usr/bin/env python3


class MenuVue:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("Accueil du gestionnaire de Tournoi:")
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
