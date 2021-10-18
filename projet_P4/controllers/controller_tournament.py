#!/usr/bin/python3
# coding: utf8
from ..modeles.modele_tournament import Tournaments
from ..vues.vue_tournament import TournamentView
from ..vues.vue import ViewMenu, UsefulView
from ..vues.vue_player import PlayerView
from datetime import datetime
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
        print(tournament)
        condition = True
        while condition:
            TournamentView.menu_tournament()
            choose_option = self.vue.saisie_chiffre(' Choisissez une option :  ')
            if choose_option == 1:
                pass
                # fonction générer un round : PAIRE DES JOUEURS
                # print(tournament['players'][0])
                # print(f'{tournament["players"][0]}', tournament['players'][5])
                # making_round = len(tournament['players']) // 2
                # print(tournament[:making_round])
                # input_score = input()

                # trier les joueurs en fonction du ranking le plus haut
                list_of_players = sorted(tournament['players'], key=itemgetter('ranking'), reverse=True)
                new_round = {
                    'name': 'Round 1',
                    'start': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
                    'end': datetime.now().strftime('%d-%m-%y %H:%M:%S'),
                    'matches': [
                        (list_of_players[0], list_of_players[4]),
                        (list_of_players[1], list_of_players[5]),
                        (list_of_players[2], list_of_players[6]),
                        (list_of_players[3], list_of_players[7]),
                    ]
                }
                TournamentView.display_pairings(new_round, list_of_players)
                Tournaments.update_tournament(new_round, int(user_input), 1)
            elif choose_option == 2:
                pass
            # DONNER DES RESULTATS INPUT SCORE
            # placer ici les input de score
             # date de fin



            elif choose_option == 3:
                condition = False

    # TournamentView.menu_tournament(tournaments=load_tournament(1), players=8)


"""  def report_menu(self):

        condition = True
        db = TinyDB('db_player.json')
        db_tournament = TinyDB('db_tournaments.json')

        while condition:
            all_players_table = db.table('players')
            players = all_players_table.all()
            all_tournaments = db_tournament.table("tournaments")
            tournaments = all_tournaments.all()
            self.vue.show_report_menu()
            choose_option = self.vue.saisie_chiffre(' Choisissez une option :  ')
            if choose_option == 1:
                list_players = sorted(players, key=itemgetter('name'))
                for player in list_players:
                    self.VuePlayer.show_player(player)
            elif choose_option == 2:
                list_players = sorted(players, key=itemgetter('ranking'))

                for player in list_players:
                    self.VuePlayer.show_player(player)
            elif choose_option == 3:
                for tournament in tournaments:
                    self.tournament.show_tournament(tournament)
            elif choose_option == 4:
                condition = False"""
