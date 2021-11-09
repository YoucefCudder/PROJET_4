#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB, Query
from ..modeles.modele_round import Round


class Tournaments:
    """class that defines what contains a tournament"""

    def __init__(self, name, place, start, end, timing, description, date, players):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.rounds = 4
        self.timing = timing
        self.description = description
        self.date = date
        self.players = players
        self.list_of_rounds = []
        self.current_round = 0

    def create_tournament(self):
        db = TinyDB("db_tournaments.json")
        tournaments_table = db.table("tournaments")

        tournaments_table.insert(
            {
                "name": self.name,
                "place": self.place,
                "start": self.start,
                "end": self.end,
                "rounds": self.rounds,
                "timing": self.timing,
                "description": self.description,
                "date": self.date,
                "players": self.players,
                "list_of_rounds": self.list_of_rounds,
            }
        )

    @staticmethod
    def deserialize_tournament():
        tournament_db = TinyDB("db_tournaments.json")
        tournament_table = tournament_db.table("tournaments")

        tournaments = []
        for item in tournament_table.all():
            tournaments.append(item)
        return tournaments

    @staticmethod
    def update_tournament():
        # trouver une fonction pour mettre a jour le tournoi avec TinyDB
        tournament_db = TinyDB("db_tournaments.json")
        r = Round("round1")
        print(tournament_db.update(Query().list_of_rounds.exists()))

    @classmethod
    def serialize_round(cls, matches, tournament):
        save_round = TinyDB("db_tournaments.json")
        save_round.update(
            {"list_of_rounds": matches}, doc_ids=[tournament]
        )
        save_round.update({"players": tournament["players"]}, doc_ids=[tournament])
        # save_round.update({'current_round': self.current_round}, doc_ids=[tournament])"""


if __name__ == "__main__":
    pass
