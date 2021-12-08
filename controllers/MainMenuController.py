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
    """class useful to handle every main controllers of the software thanks to a menu"""

    def __init__(self):
        self.menu = Menu()
        self.vue = MenuView(self.menu, "Accueil du gestionnaire de Tournoi")

    def __call__(self):
        """
        method to call the options of the main menu controller
        :return: the option called thanks to an input to make the choice
        """
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
    """class needed to handle the possibility to create a new player."""

    def __call__(self):
        """
        method to add a player via many inputs information into the database.
        :return: once it's done, the method returns the main menu controller.
        """
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
    """class needed to handle the possibility to create a new tournament."""

    def __call__(self):
        """
        method to add a tournament via  many inputs information into the database.
        :return: once it's done, the method returns the tournament controller to manage the tournament.
        """
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
    """class needed to handle the possibility to load any tournament already saved in the database."""

    def __call__(self):
        """
        method to a load a preexisting tournament saved in the database in order to manage it.
        :return: once it's done, the method returns the tournament controller
        to select specifically the tournament.
        """
        tournaments = Tournament().retrieve_all()
        if len(tournaments) <= 0:
            ErrorHandlerView().display_error("aucun tournoi à charger")
            return MainMenuController()
        return TournamentMenuController(TournamentView().select_tournament(tournaments))


class LoadReportsController:
    """class useful to call the report controllers in the main menu"""

    def __call__(self):
        """
        method to call the controller of the reports available.
        :return: it returns the report controller.
        """
        return ReportMenuController()


class ModifyPlayerController:
    """class needed to handle the possibility to modify the ranking information of a player already saved."""

    def __call__(self):
        """
        method to modify the ranking of a player.
        :return: once it's done, it returns the main menu controller
        """
        players = Player().retrieve_all()
        selected_player = PlayerView().select_player(players)
        new_ranking = InputCheckView().check_int("Nouveau classement : ")
        selected_player.ranking = new_ranking
        selected_player.update()
        return MainMenuController()


class CloseController:
    """class needed to handle the possibility to close the software"""

    def __call__(self):
        """
        method called when the user wants to close the program.
        """
        MenuView().close()
