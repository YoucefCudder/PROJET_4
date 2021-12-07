#!/usr/bin/python3
# coding: utf8
from views.ToolViews import InputCheckView


class MenuView:
    def __init__(self, menu=None, title=None):
        self.menu = menu
        self.title = title
        self.checker = InputCheckView()

    def get_user_choice(self):
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
        print("Au revoir")
