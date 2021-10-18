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

    def __repr__(self):
        return f'{self.name}, {self.f_name}, {self.ranking}'

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

    @staticmethod
    def deserialize_players():
        players_db = TinyDB('db_player.json')
        players_table = players_db.table('players')

        players = []
        for item in players_table.all():
            players.append(item)

        return players


if __name__ == '__main__':
    Player.deserialize_players()


# all_players = list()
# for player in PLAYERS_TABLE.all():
#  all_players.append(
#  Player(
#  player["name"],
# player["f_name"],
# player["gender"],
# player["birthdate"],
# player["age"],
# player["score"],
# player["ranking"],
# )
#  )

# print(all_players)
