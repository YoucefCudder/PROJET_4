#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB


class Player:
    def __init__(
        self,
        f_name=None,
        name=None,
        gender=None,
        birthdate=None,
        age=None,
        ranking=None,
    ):
        self.id = -1
        self.f_name = f_name
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = age
        self.ranking = ranking
        self.score = 0
        self.table = TinyDB("db_player.json", indent=4).table("Player")

    def __repr__(self):
        return f"{self.name} {self.f_name}, Classement: {self.ranking}"

    def __str__(self):
        return f"{self.name} {self.f_name}, Classement: {self.ranking}"

    def insert(self):
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        self.table.update(self.serialize(), doc_ids=[self.id])

    def retrieve(self, idx):
        player = self.table.get(doc_id=idx)
        self.deserialize(player)

    def retrieve_all(self):
        players = []
        for p in self.table.all():
            players.append(Player().deserialize(p))
        return players

    def serialize(self):
        return {
            "id": self.id,
            "f_name": self.f_name,
            "name": self.name,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "age": self.age,
            "ranking": self.ranking,
            "score": self.score,
        }

    def deserialize(self, p):
        self.id = p["id"]
        self.f_name = p["f_name"]
        self.name = p["name"]
        self.gender = p["gender"]
        self.birthdate = p["birthdate"]
        self.age = p["age"]
        self.ranking = p["ranking"]
        self.score = p["score"]
        return self
