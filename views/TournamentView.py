#!/usr/bin/python3
# coding: utf8
from views.ToolViews import InputCheckView, ErrorHandlerView
from pprint import pprint


class TournamentView:
    def __init__(self):
        self.checker = InputCheckView()
        self.error_handler = ErrorHandlerView()

    def create_tournament_input(self):
        print("Ajouter un nouveau tournoi: ")
        print()
        print("Placez une majuscule lors de vos saisies")

        name = self.checker.check_string("Nom: ")
        description = self.checker.check_string("Description: ")
        place = self.checker.check_string("Lieu: ")
        start = self.checker.check_date("Date de début (format DD/MM/YYYY): ")
        end = self.checker.check_date("Date de fin (format DD/MM/YYYY): ")
        timing = self.checker.time_option()

        return {
            "name": name,
            "description": description,
            "place": place,
            "start": start,
            "end": end,
            "timing": timing,
        }

    def select_players(self, players):
        selected_players = []

        while True:
            for key, player in enumerate(players):
                print(f"{key}: {player}")
            user_input = self.checker.input_in_array_of_int(
                "Votre choix: ", range(0, len(players))
            )
            selected_players.append(players[user_input])
            players.remove(players[user_input])

            if len(selected_players) == 8:
                break

        return selected_players

    def select_tournament(self, tournaments):
        for key, tournament in enumerate(tournaments):
            print(f"{key}: {tournament}")
        user_input = self.checker.input_in_array_of_int(
            "Votre choix: ", range(0, len(tournaments))
        )
        return tournaments[user_input]

    @staticmethod
    def display_match(match):
        # for m in [match if match != 0 else f"error"]:
        print(f"1.{match[0][0]} vs 2.{match[1][0]}\n")

    def result_of_match(self, match):
        self.display_match(match)
        return self.checker.result_option()

    @classmethod
    def show_tournaments(cls, tournaments):
        for t in tournaments:
            print(f"\n{t.name}  {t.place}  {t.description}  {t.start} \n")

    @classmethod
    def show_rounds_tournament(cls, tournament):

        for r in tournament.rounds_list:
            print(r)

    @classmethod
    def show_matches_tournament(cls, tournament):

        for r in tournament.rounds_list:
            print(r)
            for m in r.matches:
                print(f"1.{m[0][0]} ({m[0][1]}) vs 2.{m[1][0]} ({m[1][1]})\n")

    @classmethod
    def show_players_by_name(cls, players):
        players.sort(key=lambda x: x.name)
        for p in players:
            print(p)

    @classmethod
    def show_players_by_ranking(cls, players):
        players.sort(key=lambda x: x.ranking, reverse=True)
        for p in players:
            print(p)
