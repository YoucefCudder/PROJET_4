#!/usr/bin/python3
# coding: utf8
from ..modeles.modele_player import Player


class VuePlayer:

    def __call__(self):
        return self.create_player_input()

    @staticmethod
    def create_player_input():

        """ Input for create player & return inputs """

        f_name = input('Prénom : ')
        name = input('Nom : ')
        birthdate = input('Date de naissance (DD-MM-YYYY): ')
        genre = input('genre (M ou F) : ')
        age = input("Âge ? ")
        score = input('Score : ')
        ranking = input('Classement: ')

        Player(f_name, name, birthdate, genre, age, score, ranking)

