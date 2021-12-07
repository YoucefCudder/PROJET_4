#!/usr/bin/python3
# coding: utf8
from datetime import datetime
from models.Player import Player


class Round:
    def __init__(self, name=None):
        self.name = name
        self.start_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.end_time = None
        self.matches = []

    def __repr__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"

    def serialize(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [
                ([m[0][0].serialize(), m[0][1]], [m[1][0].serialize(), m[1][1]])
                for m in self.matches
            ],
        }

    def deserialize(self, r):
        self.name = r["name"]
        self.start_time = r["start_time"]
        self.end_time = r["end_time"]
        self.matches = [
            (
                [Player().deserialize(m[0][0]), m[0][1]],
                [Player().deserialize(m[1][0]), m[1][1]],
            )
            for m in r["matches"]
        ]
        return self

    def first_pairing(self, players):
        sorted_list = sorted(players, key=lambda p: int(p.ranking), reverse=True)
        print(sorted_list)
        self.matches = [
            ([sorted_list[0], -1], [sorted_list[4], -1]),
            ([sorted_list[1], -1], [sorted_list[5], -1]),
            ([sorted_list[2], -1], [sorted_list[6], -1]),
            ([sorted_list[3], -1], [sorted_list[7], -1]),
        ]

    def other_pairing(self, players, rounds):
        sorted_list = sorted(
            players, key=lambda p: (float(p.score), int(p.ranking)), reverse=True
        )
        match_already_happened = False

        for r in rounds:
            for m in r.matches:
                if (
                    m[0][0].id == sorted_list[0].id and m[1][0].id == sorted_list[1].id
                ) or (
                    m[1][0].id == sorted_list[0].id and m[0][0].id == sorted_list[1].id
                ):
                    match_already_happened = True

        if match_already_happened:
            self.matches = [
                ([sorted_list[0], -1], [sorted_list[2], -1]),
                ([sorted_list[1], -1], [sorted_list[3], -1]),
                ([sorted_list[4], -1], [sorted_list[5], -1]),
                ([sorted_list[6], -1], [sorted_list[7], -1]),
            ]
        else:
            self.matches = [
                ([sorted_list[0], -1], [sorted_list[1], -1]),
                ([sorted_list[2], -1], [sorted_list[3], -1]),
                ([sorted_list[4], -1], [sorted_list[5], -1]),
                ([sorted_list[6], -1], [sorted_list[7], -1]),
            ]

    def end_round(self):
        self.end_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
