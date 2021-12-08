#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB
from models.Player import Player
from models.Round import Round


class Tournament:
    """class needed to conceptualize the model of a tournament in the software and its place in the database."""

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
        """method useful to serialize, which means that stores the tournament in the database with an id"""
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        """method useful to update the tournament in the database with new information"""
        self.table.update(self.serialize(), doc_ids=[self.id])

    def retrieve(self, idx):
        """method useful to retrieve a tournament from the database thanks to the id"""
        tournament = self.table.get(doc_id=idx)
        self.deserialize(tournament)

    def retrieve_all(self):
        """method useful to retrieve all the tournaments from the database"""
        tournaments = []
        for t in self.table.all():
            tournaments.append(Tournament().deserialize(t))
        return tournaments

    def serialize(self):
        """method that shows what to serialize about the tournament"""
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
        """method method to deserialize a tournament and using it as an instance."""
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
