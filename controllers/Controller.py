#!/usr/bin/python3
# coding: utf8
from controllers.MainMenuController import MainMenuController


class Controller:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = MainMenuController()
        while self.controller:
            self.controller = self.controller()
