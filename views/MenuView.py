#!/usr/bin/python3
# coding: utf8
from views.ToolViews import InputCheckView


class MenuView:
    """class that displays the view of the menu and handle the input of the user."""

    def __init__(self, menu=None, title=None):
        self.menu = menu
        self.title = title
        self.checker = InputCheckView()

    def get_user_choice(self):
        """method useful to display the menu options and handle
        the choice of the user via the input."""
        print(self.title)
        print()

        while True:
            menu_items = self.menu.items()
            for key, entry in menu_items:
                print(f"{key}: {entry.option}")
            user_choice = input(">> ")
            if user_choice in self.menu:
                return self.menu[user_choice]

    @staticmethod
    def close():
        """method to print a message when the user choose to close the program."""
        print("Au revoir")
