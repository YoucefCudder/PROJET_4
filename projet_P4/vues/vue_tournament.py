#!/usr/bin/python3
# coding: utf8
from projet_P4.modeles.modele_tournament import Tournaments
from datetime import datetime


class TournamentView:

    @staticmethod
    def create_tournament():
        print("Créer un noouveau tournoi :")
        print()

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

    @staticmethod
    def show_tournament(tournament):
        print(f'{tournament["name"]} - {tournament["place"]},  {tournament["date"]}  {tournament["description"]}')
