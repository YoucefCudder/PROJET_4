#!/usr/bin/python3
# coding: utf8
from views.ToolViews import InputCheckView, ErrorHandlerView


class TournamentView:
    """class that handle what the user can see about everything related to the tournament."""

    def __init__(self):
        self.checker = InputCheckView()
        self.error_handler = ErrorHandlerView()

    def create_tournament_input(self):
        """method useful to propose inputs in order to create a tournament according to the user"""
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
        """method to select players who participate in the tournament."""
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
        """method useful when it comes to select a tournament."""
        for key, tournament in enumerate(tournaments):
            print(f"{key}: {tournament}")
        user_input = self.checker.input_in_array_of_int(
            "Votre choix: ", range(0, len(tournaments))
        )
        return tournaments[user_input]

    @classmethod
    def display_match(cls, match):
        """method useful to display the format of a match."""
        print(f"1.{match[0][0]} vs 2.{match[1][0]}\n")

    def result_of_match(self, match):
        """method useful when it comes to determine the score of a match."""
        self.display_match(match)
        return self.checker.result_option()

    @classmethod
    def show_tournaments(cls, tournaments):
        """method to show properly a tournament."""
        for t in tournaments:
            print(f"\n{t.name}  {t.place}  {t.description}  {t.start} \n")

    @classmethod
    def show_rounds_tournament(cls, tournament):
        """method to show rounds of a tournament."""
        for r in tournament.rounds_list:
            print(r)

    @classmethod
    def show_matches_tournament(cls, tournament):
        """method to show the matches of a tournament."""
        for r in tournament.rounds_list:
            print(r)
            for m in r.matches:
                print(f"1.{m[0][0]} ({m[0][1]}) vs 2.{m[1][0]} ({m[1][1]})\n")

    @classmethod
    def show_players_by_name(cls, players):
        """method to show players sorted by name."""
        players.sort(key=lambda x: x.name)
        for p in players:
            print(p)

    @classmethod
    def show_players_by_ranking(cls, players):
        """method to show players sorted by ranking."""
        players.sort(key=lambda x: x.ranking, reverse=True)
        for p in players:
            print(p)
