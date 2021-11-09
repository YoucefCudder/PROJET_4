#!/usr/bin/python3
# coding: utf8
from datetime import datetime
from tinydb import TinyDB


class Round:
    def __init__(self, round_name):
        self.round_name = round_name
        self.start_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.end_time = None
        self.matches = []

    def round_info(self):
        return [self.round_name, self.start_time, self.end_time, self.matches]

    def pairing_for_round(self, player_1, player_2):
        """Set match paring as tuple"""
        print(type(player_2))
        print(type(player_1['f_name']))
        match = (
            f" PRENOM : {player_1['f_name']}, NOM : {player_1['name']}, CLASSEMENT : {player_1['ranking']},"
            f" SCORE :  {player_1['score']}",
            f" VS PRENOM {player_2['f_name']},NOM {player_2['name']}, CLASSEMENT : {player_2['ranking']},"
            f" SCORE : {player_2['score']}",
        )

