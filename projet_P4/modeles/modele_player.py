#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB


class Player:
    """class to define what compose the information's player and what a player does"""

    def __init__(self, f_name, name, gender, birthdate, age, score, ranking):
        self.f_name = f_name
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = age
        self.score = score
        self.ranking = ranking

    def create_players(self):
        db = TinyDB('db_player.json')
        players_table = db.table('players')
        players_table.insert({
            'name': self.name,
            'f_name': self.f_name,
            'gender': self.gender,
            'birthdate': self.birthdate,
            'age': self.age,
            'score': self.score,
            'ranking': self.ranking
        })




