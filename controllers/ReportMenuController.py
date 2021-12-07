#!/usr/bin/python3
# coding: utf8
import controllers.MainMenuController
from models.Menu import Menu
from views.MenuView import MenuView
from models.Player import Player
from models.Tournament import Tournament
from views.TournamentView import TournamentView
from views.ToolViews import InputCheckView, ReportView


class ReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.vue = MenuView(
            self.menu, "\nAffichage des différents rapports disponibles\n"
        )

    def __call__(self):
        self.menu.add("auto", "Affichage de tous les joueurs", GeneralPlayerReport())
        self.menu.add("auto", "Affichage des joueurs par tournoi", PlayersTournament())
        self.menu.add("auto", "Affichage des tournois", TournamentReport())
        self.menu.add(
            "auto",
            "Retour au menu principal",
            controllers.MainMenuController.MainMenuController(),
        )

        user_choice = self.vue.get_user_choice()

        return user_choice.handler


class GeneralPlayerReport:
    def __call__(self):
        players_data = Player().retrieve_all()
        ReportView().show_options()
        user_choice = InputCheckView().input_int("Veuillez choisir une option : \n")
        if user_choice == 1:
            TournamentView.show_players_by_name(players_data)
            return ReportMenuController()
        elif user_choice == 2:
            TournamentView.show_players_by_ranking(players_data)
            return ReportMenuController()

        else:
            return ReportMenuController()


class PlayersTournament:
    def __call__(self):
        tournament_data = Tournament().retrieve_all()
        select_tournament = TournamentView().select_tournament(tournament_data)

        players_data = select_tournament.players
        ReportView().show_options()
        user_choice = InputCheckView().input_int("Veuillez choisir une option : \n")
        if user_choice == 1:
            TournamentView.show_players_by_name(players_data)
            return ReportMenuController()
        elif user_choice == 2:
            TournamentView.show_players_by_ranking(players_data)
            return ReportMenuController()
        return ReportMenuController()


class TournamentReport:
    def __call__(self):
        tournament_data = Tournament().retrieve_all()
        select_tournament = TournamentView().select_tournament(tournament_data)
        ReportView().show_options_for_tournament()
        user_choice = InputCheckView().input_int("Veuillez choisir une option : \n")
        if user_choice == 1:
            TournamentView().show_tournaments(tournament_data)
        elif user_choice == 2:
            TournamentView().show_matches_tournament(select_tournament)
        elif user_choice == 3:
            TournamentView().show_rounds_tournament(select_tournament)
        return ReportMenuController()
