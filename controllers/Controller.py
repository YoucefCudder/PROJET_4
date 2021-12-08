#!/usr/bin/python3
# coding: utf8
from controllers.MainMenuController import MainMenuController


class Controller:
    """class useful to start the program"""

    def __init__(self):
        self.controller = None

    def start(self):
        """start the program, redirect to a menu controller while it's needed"""
        self.controller = MainMenuController()
        while self.controller:
            self.controller = self.controller()
