#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB, Query


class Tournaments:
    """class that defines what contains a tournament 
    """

    def __init__(self, name, place, start, end, rounds, timing, description, date, players):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.rounds = rounds
        self.timing = timing
        self.description = description
        self.date = date
        self.players = players
        self.list_of_rounds = []
        self.current_round = 0

    def create_tournament(self):
        db = TinyDB('db_tournaments.json')
        tournaments_table = db.table('tournaments')

        tournaments_table.insert({
            'name': self.name,
            'place': self.place,
            'start': self.start,
            'end': self.end,
            'rounds': self.rounds,
            'timing': self.timing,
            'description': self.description,
            'date': self.date,
            'players': self.players,
            'list_of_rounds': self.list_of_rounds

        })

    @staticmethod
    def deserialize_tournament():
        tournament_db = TinyDB('db_tournaments.json')
        tournament_table = tournament_db.table('tournaments')

        tournaments = []
        for item in tournament_table.all():
            tournaments.append(item)
        return tournaments

    @staticmethod
    def update_tournament(new_round, tournament_id, current_round):
        # trouver une fonction pour mettre a jour le tournoi avec TinyDB
        tournament_db = TinyDB('db_tournaments.json')
        tournament_db.update({'list_of_rounds': new_round}, doc_ids=[tournament_id])
        tournament_db.update({'current_round': current_round}, doc_ids=[tournament_id])


