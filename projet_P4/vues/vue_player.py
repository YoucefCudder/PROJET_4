#!/usr/bin/python3
# coding: utf8
from ..modeles.modele_player import Player


class PlayerView:

    @staticmethod
    def create_player_input():
        """ Input for create player & return inputs """
        print("Ajouter un nouveau joueur :  ")
        print()


        f_name = input('Prénom : ')
        name = input('Nom : ')
        genre = input('genre (M ou F) : ')
        birthdate = input('Date de naissance (DD-MM-YYYY): ')
        age = input("Âge ? ")
        score = input('Score : ')
        ranking = input('Classement: ')

        Player(f_name, name, birthdate, genre, age, score, ranking).create_players()


    @staticmethod
    def show_player(player):
        print(f'{player["name"]} - {player["f_name"]},  Classement : {player["ranking"]}')




