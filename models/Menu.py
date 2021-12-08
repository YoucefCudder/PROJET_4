#!/usr/bin/python3
# coding: utf8
class Menu:
    """
    class that create a menu system for multiple parts of the program.
    """

    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, handler):
        """method to generate a new menu option with a systeme based on a key, an option and a handler"""
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        self._entries[str(key)] = MenuEntry(option, handler)

    def items(self):
        """Returns a dictionary of entries added to the menu"""
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]


class MenuEntry:
    """class that handle the input of the user when it comes to using the different menus"""

    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    def __repr__(self):
        return f"MenuEntry({self.option}, {self.handler})"

    def __str__(self):
        return str(self.option)
