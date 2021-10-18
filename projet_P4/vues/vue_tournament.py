#!/usr/bin/python3
# coding: utf8
from datetime import datetime
from ..controllers.controller_player import PlayersControl
from ..modeles.modele_tournament import Tournaments
from ..vues.vue import UsefulView


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
        players = PlayersControl().select_players(players_total=8)
        Tournaments(name, place, start, end, timing, rounds,
                    description, date, players).create_tournament()

    @staticmethod
    def show_tournament(tournament):
        print(f'{tournament["name"]} - {tournament["place"]},'
              f'  {tournament["date"]}  {tournament["description"]}')

    @staticmethod
    def select_tournament(tournaments):
        print(f"\n Choisissez un tournoi :\n")
        for i in range(len(tournaments)):
            print(f"[{tournaments[i].doc_id}]", end=' ')
            print(f"{tournaments[i]['name']}, {tournaments[i]['place']}", end=" | ")
            print(f"{tournaments[i]['start']} | {tournaments[i]['end']}", end=" | \n")
            # print(f"Joueurs au tournoi : {tournaments[i]['players']}")

        print("\n[back] Retour au menu")

    @staticmethod
    def menu_tournament():
        print("1 -  lancer un round")
        print("2 - terminer un round, afficher le rapport")
        print("3 - Retour au menu principal")

    @staticmethod
    def display_pairings(new_round, list_of_players):
        print(f'Nom du round:  {new_round["name"]}\n\n')
        print(f'Date de début: {new_round["start"]}\n')
        print(f'Date de fin:   {new_round["end"]}\n')
        #
        # i = f'{new_round["matches"][0][0]}, {new_round["matches"][0][0]}'
        print()
        for match, match_1 in new_round['matches']:
            print(f'{match["name"]}  {match["f_name"]}    {match["ranking"]}  VS   '
                  f'{match_1["name"]}  {match_1["f_name"]}   {match_1["ranking"]}')
            print(match['name'], match['ranking'], match_1['name'], match_1['ranking'])
        # for i in match, match_1:
            score_1 = input(f'le score de {match["name"]}:  ')
            score_2 = input(f'le score de {match_1["name"]}: ')

    # print(f'les matchs du round: ', match)
    # for score in match:
    #

    # print({list_of_players[0]['name']}, {list_of_players[0]['ranking']}, {list_of_players[3]['name']},
    # {list_of_players[3]['ranking']})
    # print({list_of_players[1]['name']}, {list_of_players[1]['ranking']}, {list_of_players[5]['name']},
    # {list_of_players[5]['ranking']})
    # print({list_of_players[2]['name']}, {list_of_players[2]['ranking']}, {list_of_players[6]['name']},
    # {list_of_players[6]['ranking']})
    # print({list_of_players[3]['name']}, {list_of_players[3]['ranking']}, {list_of_players[7]['name']},
    # {list_of_players[7]['ranking']})

    def input_score(self, message):
        UsefulView.saisie_chiffre(message)
