#!/usr/bin/python3
# coding: utf8
from datetime import datetime


class Round:
    def __init__(self, round_name):
        self.round_name = round_name
        self.start_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        self.end_time = None
        self.matches = []

    def round_info(self):
        return [
            self.round_name,
            self.start_time,
            self.end_time,
            self.matches
        ]

    def pairing_for_round(self, player_1, player_2):
        """Set match paring as tuple"""
        match = (
            f"{player_1['f_name']}, {player_1['name']}",
            player_1["ranking"],
            player_1["score"],
            f"{player_2['f_name']}, {player_2['name']}",
            player_2["ranking"],
            player_2["score"]
        )
        self.matches.append(match)

