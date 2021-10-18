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

    # A TESTER

    @staticmethod
    def select_players(players, player_number):
        print(f"\nSelect player {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i].doc_id}]", end=' ')
            print(f"{players[i]['name']}, {players[i]['f_name']}", end=" | ")
            print(f"{players[i]['gender']} | {players[i]['birthdate']}", end=" | ")
            print(f"Rank : {players[i]['ranking']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def player_already_selected():
        print("\nPlayer already selected. Please select other player.")


