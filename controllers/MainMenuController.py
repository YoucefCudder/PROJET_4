#!/usr/bin/python3
# coding: utf8
from controllers.TournamentMenuController import TournamentMenuController
from models.Menu import Menu
from models.Player import Player
from models.Tournament import Tournament
from views.MenuView import MenuView
from views.PlayerView import PlayerView
from views.ToolViews import ErrorHandlerView, InputCheckView
from views.TournamentView import TournamentView
from controllers.ReportMenuController import ReportMenuController


class MainMenuController:
    def __init__(self):
        self.menu = Menu()
        self.vue = MenuView(self.menu, "Accueil du gestionnaire de Tournoi")

    def __call__(self):
        self.menu.add("auto", "Ajouter un joueur\n", AddPlayerController())
        self.menu.add("auto", "Créer un tournoi\n", AddTournamentController())
        self.menu.add("auto", "Charger un tournoi\n", LoadTournamentController())
        self.menu.add("auto", "Modifier un joueur\n", ModifyPlayerController())
        self.menu.add(
            "auto",
            "Accéder aux différents rapports (joueurs/tournois)\n",
            LoadReportsController(),
        )
        self.menu.add("auto", "Quitter le programme", CloseController())

        user_choice = self.vue.get_user_choice()

        return user_choice.handler


class AddPlayerController:
    def __call__(self):
        player_data = PlayerView().create_player_input()
        player = Player(
            player_data["f_name"],
            player_data["name"],
            player_data["gender"],
            player_data["birthdate"],
            player_data["age"],
            player_data["ranking"],
        )
        player.insert()
        return MainMenuController()


class AddTournamentController:
    def __call__(self):
        tournament_data = TournamentView().create_tournament_input()
        tournament = Tournament(
            tournament_data["name"],
            tournament_data["description"],
            tournament_data["place"],
            tournament_data["start"],
            tournament_data["end"],
            tournament_data["timing"],
        )
        tournament.players = TournamentView().select_players(Player().retrieve_all())
        tournament.insert()
        return TournamentMenuController(tournament)


class LoadTournamentController:
    def __call__(self):
        tournaments = Tournament().retrieve_all()
        if len(tournaments) <= 0:
            ErrorHandlerView().display_error("aucun tournoi à charger")
            return MainMenuController()
        return TournamentMenuController(TournamentView().select_tournament(tournaments))


class LoadReportsController:
    def __call__(self):
        return ReportMenuController()


class ModifyPlayerController:
    def __call__(self):
        players = Player().retrieve_all()
        selected_player = PlayerView().select_player(players)
        new_ranking = InputCheckView().input_int("Nouveau classement : ")  # vue
        selected_player.ranking = new_ranking
        selected_player.update()
        return MainMenuController()


class CloseController:
    def __call__(self):
        MenuView().close()
