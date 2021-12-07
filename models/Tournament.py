#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB
from models.Player import Player
from models.Round import Round


class Tournament:
    def __init__(
        self, name=None, description=None, place=None, start=None, end=None, timing=None
    ):
        self.id = -1
        self.name = name
        self.description = description
        self.place = place
        self.start = start
        self.end = end
        self.timing = timing
        self.rounds = 4
        self.rounds_list = []
        self.current_round = 0
        self.players = []
        self.table = TinyDB("db_tournament.json", indent=4).table("Tournament")

    def __repr__(self):
        return f"{self.name} - {self.place} ({self.start} - {self.end})"

    def __str__(self):
        return f"{self.name} - {self.place} ({self.start} - {self.end})"

    def insert(self):
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        self.table.update(self.serialize(), doc_ids=[self.id])

    def retrieve(self, idx):
        tournament = self.table.get(doc_id=idx)
        self.deserialize(tournament)

    def retrieve_all(self):
        tournaments = []
        for t in self.table.all():
            tournaments.append(Tournament().deserialize(t))
        return tournaments

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "place": self.place,
            "start": self.start,
            "end": self.end,
            "timing": self.timing,
            "rounds": self.rounds,
            "rounds_list": [r.serialize() for r in self.rounds_list],
            "current_round": self.current_round,
            "players": [p.serialize() for p in self.players],
        }

    def deserialize(self, t):
        self.id = t["id"]
        self.name = t["name"]
        self.description = t["description"]
        self.place = t["place"]
        self.start = t["start"]
        self.end = t["end"]
        self.timing = t["timing"]
        self.rounds = t["rounds"]
        self.rounds_list = [Round().deserialize(r) for r in t["rounds_list"]]
        self.current_round = t["current_round"]
        self.players = [Player().deserialize(p) for p in t["players"]]
        return self
