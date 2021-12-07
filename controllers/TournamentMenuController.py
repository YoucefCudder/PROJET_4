#!/usr/bin/python3
# coding: utf8
import controllers.MainMenuController
from models.Menu import Menu
from models.Round import Round
from views.MenuView import MenuView
from views.TournamentView import TournamentView
from views.ToolViews import ErrorHandlerView, ReportView, InputCheckView


class TournamentMenuController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.vue = MenuView(self.menu, "")
        self.tournament = tournament

    def __call__(self):
        self.menu.add("auto", "Lancer un round", StartRoundController(self.tournament))
        self.menu.add("auto", "Terminer un round", EndRoundController(self.tournament))
        self.menu.add(
            "auto", "Afficher les matchs", ShowMatchController(self.tournament)
        )
        self.menu.add(
            "auto",
            "Afficher les matchs/rounds",
            ShowTournamentContentController(self.tournament),
        )
        self.menu.add("auto", "Retour au menu principal", ReturnController())

        user_choice = self.vue.get_user_choice()

        return user_choice.handler


class StartRoundController:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self):
        if (
            self.tournament.current_round >= self.tournament.rounds
            and self.tournament.rounds_list[self.tournament.current_round - 1].end_time
            is not None
        ):
            ErrorHandlerView().display_error("tournoi déjà terminé")
        elif (
            self.tournament.current_round > 0
            and self.tournament.rounds_list[self.tournament.current_round - 1].end_time
            is None
        ):
            ErrorHandlerView().display_error("un round est en cours")
        else:
            self.tournament.current_round += 1
            new_round = Round(f"Round {self.tournament.current_round}")
            if self.tournament.current_round == 1:
                new_round.first_pairing(self.tournament.players)
            else:
                new_round.other_pairing(
                    self.tournament.players, self.tournament.rounds_list
                )
            self.tournament.rounds_list.append(new_round)
            self.tournament.update()

            for match in new_round.matches:
                TournamentView().display_match(match)

        return TournamentMenuController(self.tournament)


class EndRoundController:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self):
        if (
            self.tournament.current_round >= self.tournament.rounds
            and self.tournament.rounds_list[self.tournament.current_round - 1].end_time
            is not None
        ):
            ErrorHandlerView().display_error("tournoi déjà terminé")
        elif (
            self.tournament.current_round > 0
            and self.tournament.rounds_list[self.tournament.current_round - 1].end_time
            is not None
        ):
            ErrorHandlerView().display_error("aucun round en cours")
        else:
            self.tournament.rounds_list[self.tournament.current_round - 1].end_round()
            for match in self.tournament.rounds_list[
                self.tournament.current_round - 1
            ].matches:
                player_1_idx = -1
                player_2_idx = -1

                for idx, player in enumerate(self.tournament.players):
                    if player.id == match[0][0].id:
                        player_1_idx = idx
                    if player.id == match[1][0].id:
                        player_2_idx = idx

                result = TournamentView().result_of_match(match)
                if result == "1":
                    self.tournament.players[player_1_idx].score += 1
                    match[0][1] = 1
                    match[1][1] = 0
                elif result == "2":
                    self.tournament.players[player_2_idx].score += 1
                    match[0][1] = 0
                    match[1][1] = 1
                else:
                    self.tournament.players[player_1_idx].score += 0.5
                    self.tournament.players[player_2_idx].score += 0.5
                    match[0][1] = 0.5
                    match[1][1] = 0.5

            self.tournament.update()

        return TournamentMenuController(self.tournament)


class ShowMatchController:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self):
        TournamentView().show_matches_tournament(self.tournament)
        return TournamentMenuController(self.tournament)


class ShowTournamentContentController:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self):
        ReportView().show_options_for_tournament()
        user_choice = InputCheckView().input_int("Veuillez choisir une option : \n")
        if user_choice == 1:
            TournamentView().show_matches_tournament(self.tournament)
        elif user_choice == 2:
            TournamentView().show_rounds_tournament(self.tournament)
        return TournamentMenuController(self.tournament)


class ReturnController:
    def __call__(self):
        return controllers.MainMenuController.MainMenuController()
