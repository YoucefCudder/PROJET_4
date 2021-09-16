#!/usr/bin/python3
# coding: utf8
from ..modeles.modele_tournament import Tournaments
from datetime import datetime


class TournamentControl:

    def __call__(self, *args, **kwargs):
        return create_tournament()


def create_tournament():
    date = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    name = input('Name: ')
    place = input('Place: ')
    start = input('Start: ')
    end = input('End: ')
    rounds = input('Rounds:  ')
    timing = input('Timing:  ')
    description = input('Description: ')

    Tournaments(name, place, start, end, timing, rounds,
                description, date).creer_tournoi()

# nouveau_tournoi = TournamentControl().create_tournament

# Tournaments(name=nouveau_tournoi['name'], place=nouveau_tournoi['place'], start=nouveau_tournoi['start'],
#    end=nouveau_tournoi['end'], rounds=nouveau_tournoi['rounds'], timing=nouveau_tournoi['timing'],
#   description=nouveau_tournoi['description'], date=nouveau_tournoi['date']).create_tournament()
