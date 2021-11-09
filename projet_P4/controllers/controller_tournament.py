#!/usr/bin/python3
# coding: utf8
from ..modeles.modele_tournament import Tournaments

from ..modeles.modele_round import Round
from ..vues.vue_tournament import TournamentView
from ..vues.vue import ViewMenu, UsefulView
from ..vues.vue_player import PlayerView

# from datetime import datetime
from operator import itemgetter


class TournamentControl:
    """
    doctstring
    """

    def __init__(self):
        self.view_player = PlayerView()
        self.view_tournament = TournamentView()
        self.vue = UsefulView()
        self.menu = ViewMenu(menu=None)

    def load_tournament(self):
        tournaments = Tournaments.deserialize_tournament()
        id_list = []
        for i in range(len(tournaments)):
            id_list.append(tournaments[i].doc_id)
        TournamentView.select_tournament(tournaments)
        self.vue.input_prompt()
        user_input = input()
        tournament = tournaments[id_list.index(int(user_input))]
        condition = True
        while condition:
            TournamentView.menu_tournament()
            choose_option = self.vue.input_int(" Choisissez une option :  ")
            # trier les joueurs en fonction du ranking le plus haut
            list_of_players = sorted(
                tournament["players"], key=itemgetter("ranking"), reverse=True
            )

            if choose_option == 1:

                # fonction générer un round : PAIRE DES JOUEURS
                # INSTANCE DE CLASSE ROUND
                TournamentView.display_pairings(list_of_players[0], list_of_players[4])

                TournamentView.display_pairings(list_of_players[1], list_of_players[5])
                TournamentView.display_pairings(list_of_players[2], list_of_players[6])
                TournamentView.display_pairings(list_of_players[3], list_of_players[7])

                # Enregistrer le ROUND dans le TOURNOI dans TINYDB

            elif choose_option == 2:
                # DONNER DES RESULTATS INPUT SCORE
                # placer ici les input de score
                # date de fin

                Tournaments.serialize_round(
                    tournament=tournament,
                    matches=Round.pairing_for_round(tournament, list_of_players[0], list_of_players[4]),
                )

                TournamentView.input_score(list_of_players[0], list_of_players[4])

                # enregistrer le score des JOUEURS dans le TOURNOI dans TINYDB

            elif choose_option == 3:
                TournamentView.reports_intra_tournament()
                option_chosen = self.vue.input_int(" Choisissez une option :  ")
                if option_chosen == 1:
                    list_of_sorted_players = sorted(
                        tournament["players"], key=itemgetter("name")
                    )
                    TournamentView.show_player(list_of_sorted_players, tournament)
                elif option_chosen == 2:
                    list_of_ranked_players = sorted(
                        tournament["players"], key=itemgetter("score"), reverse=True
                    )
                    TournamentView.show_player_ranked(
                        list_of_ranked_players, tournament
                    )
                elif option_chosen == 3:
                    TournamentView.show_rounds(tournament)
                elif option_chosen == 3:
                    pass
                elif option_chosen == 3:
                    condition = False

            elif choose_option == 4:

                condition = False
                """new_round = {
                    'name': 'Round 1',
                    'start': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
                    'end': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
                    'matches': [
                        (list_of_players[0], list_of_players[4]),
                        (list_of_players[1], list_of_players[5]),
                        (list_of_players[2], list_of_players[6]),
                        (list_of_players[3], list_of_players[7]),
                    ]
                }"""
