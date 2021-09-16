#!/usr/bin/env python3
from ..vues.vue import MenuVue
from ..modeles.model import Menu
from ..controllers.controller_tournament import TournamentControl
from ..controllers.controller_player import PlayersControl
from ..vues.vue_player import VuePlayer


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
        self.vue = MenuVue(self.menu)

    def __call__(self):
        # construction du menu
        self.menu.add("auto", "créer un tournoi", NouveauTournoiController())
        self.menu.add("auto", "accéder au classement", RankingController())
        self.menu.add("auto", "ajouter un joueur", AjouterJoueurController())

        # demande d'affichage du menu et collecte de réponse
        user_choice = self.vue.get_user_choice()

        # renvoyer le controller correspondant
        return user_choice.handler


class NouveauTournoiController:
    def __call__(self):
        print("Créer un noouveau tournoi :")
        TournamentControl()


class RankingController:

    def __call__(self):
        print("Affichage du ranking")
        return MenuController()


class AjouterJoueurController:

    def __call__(self):
        print("Ajouter un nouveau joueur :")
        PlayersControl()
