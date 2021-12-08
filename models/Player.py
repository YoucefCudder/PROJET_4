#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB


class Player:
    """class needed to conceptualize the model of a player in the software and its place in the database."""

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
        """method to insert  the player in the database with and id."""
        self.id = self.table.insert(self.serialize())
        self.update()

    def update(self):
        """method to update the player in the database."""
        self.table.update(self.serialize(), doc_ids=[self.id])

    def retrieve(self, idx):
        """method to retrieve the player thanks to the id."""
        player = self.table.get(doc_id=idx)
        self.deserialize(player)

    def retrieve_all(self):
        """method to retrieve all players stored in the database, and deserialize them."""
        players = []
        for p in self.table.all():
            players.append(Player().deserialize(p))
        return players

    def serialize(self):
        """method useful to serialize a player in the database."""
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
        """method to deserialize a player and using it as an instance."""
        self.id = p["id"]
        self.f_name = p["f_name"]
        self.name = p["name"]
        self.gender = p["gender"]
        self.birthdate = p["birthdate"]
        self.age = p["age"]
        self.ranking = p["ranking"]
        self.score = p["score"]
        return self
