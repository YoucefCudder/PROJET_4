#!/usr/bin/env python3
from ..vues.vue import ViewMenu
from ..modeles.model import Menu
from projet_P4.vues.vue_tournament import TournamentView
# from ..controllers.controller_player import PlayersControl
from ..vues.vue_player import PlayerView
from tinydb import TinyDB
from operator import itemgetter


class Controller:

    def __init__(self):
        self.controller = None

    def start_menu(self):
        self.controller = MenuController()
        while self.controller:
            self.controller = self.controller()


class MenuController:

    def __init__(self):
        self.menu = Menu()
        self.vue = ViewMenu(self.menu)

    def __call__(self):
        # construction du menu
        self.menu.add("auto", "Créer un tournoi", NouveauTournoiController())
        self.menu.add("auto", "Accéder aux différents rapports (joueurs/tournois)", RankingController())
        self.menu.add("auto", "Ajouter un joueur", AjouterJoueurController())

        # demande d'affichage du menu et collecte de réponse
        user_choice = self.vue.get_user_choice()

        # renvoyer le controller correspondant
        return user_choice.handler


class NouveauTournoiController:
    def __call__(self):
        TournamentView().create_tournament()
        """ ****CREER LA POSSIBILITE DE CHOISIR SES JOUEURS *****"""


        return MenuController()


class RankingController:

    def __init__(self):
        self.VuePlayer = PlayerView()
        self.vue = ViewMenu(self)
        self.tournament = TournamentView()

    def __call__(self):
        RankingController().report_menu()
        return MenuController()

    def report_menu(self):

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
                condition = False


class AjouterJoueurController:

    def __call__(self):
        PlayerView().create_player_input()

        return MenuController()
