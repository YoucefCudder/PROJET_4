#!/usr/bin/python3
# coding: utf8
from datetime import datetime
from ..controllers.controller_player import PlayersControl
from ..modeles.modele_tournament import Tournaments
from ..modeles.modele_round import Round
from ..vues.vue import UsefulView
from ..controllers.controller import MenuController

class TournamentView:
    @staticmethod
    def create_tournament():
        print("Créer un noouveau tournoi :")
        print("\n")
        print("Placez une majuscule lors de vos saisies")

        date = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        name = input("Name: ")
        place = input("Place: ")
        start = input("Start: ")
        end = input("End: ")
        timing = UsefulView.time_control_options()

        description = input("Description: ")
        players = PlayersControl().select_players(players_total=8)
        UsefulView.confirmation_input()
        Tournaments(
            name, place, start, end, timing, description, date, players
        ).create_tournament()

    @classmethod
    def show_tournament(cls, tournament):
        print(
            f'{tournament["name"]} - {tournament["place"]},'
            f'  {tournament["date"]}  {tournament["description"]}'
        )

    @staticmethod
    def select_tournament(tournaments):
        print(f"\n Choisissez un tournoi :\n")
        for i in range(len(tournaments)):
            print(f"[{tournaments[i].doc_id}]", end=" ")
            print(f"{tournaments[i]['name']}, {tournaments[i]['place']}", end=" | ")
            print(f"{tournaments[i]['start']} | {tournaments[i]['end']}", end=" | \n")
            # print(f"Joueurs au tournoi : {tournaments[i]['players']}")

        print("\n[back] Retour au menu")

    def input_time_control(self):

        UsefulView.time_control_options()
        UsefulView.input_prompt()
        user_input = input()

        if user_input == "1":
            return "Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Rapid"
        elif user_input == "back":
            MenuController()
        else:
            UsefulView.input_error()
            self.input_time_control()

    @classmethod
    def menu_tournament(cls):
        print("1 -  Lancer un round")
        print("2 -  Terminer le round, entrer les scores")
        print("3 -  Afficher le rapport")
        print("4 -  Retour au menu principal")

    @classmethod
    def reports_intra_tournament(cls):
        print(
            "1- Afficher le classement des joueurs d'un tournoi par ordre alphabétique"
        )
        print("2- Afficher le classement des joueurs d'un tournoi par le score")
        print("3- Afficher la liste des rounds d'un tournoi")
        print("4- Afficher la liste des matchs d'un tournoi")

    @classmethod
    def show_player(cls, list_of_sorted_players, tournament):
        print(
            f'Classement des joueurs du tournoi {tournament["name"]} {tournament["place"]}'
        )
        for player_name in list_of_sorted_players:
            print(
                f'Nom {player_name["name"]} |  Prénom  {player_name["f_name"]}'
                f' | Classement : {player_name["ranking"]}'
            )

    @classmethod
    def show_player_ranked(cls, list_of_ranked_players, tournament):
        print(
            f'Classement des joueurs du tournoi {tournament["name"]} {tournament["place"]}'
        )
        for player_score in list_of_ranked_players:
            print(
                f'Nom {player_score["name"]} |  Prénom  {player_score["f_name"]} | Score : {player_score["score"]}'
            )

    @classmethod
    def show_rounds(cls, tournament):
        print(
            f'Classement des joueurs du tournoi {tournament["name"]} {tournament["place"]}'
        )
        for rounds in tournament["list_of_rounds"]:
            print(f"{rounds}")

    @classmethod
    def input_score(cls, player_1, player_2):
        print(
            f' Nom : {player_1["name"]},   Prénom : {player_1["f_name"]} |   Classement :  {player_1["ranking"]}  VS'
            f' Nom : {player_2["name"]}, Prénom : {player_2["f_name"]} | Classement :   {player_2["ranking"]}'
        )
        score_1 = input(f'le score de {player_1["name"]}:  ')
        score_2 = input(f'le score de {player_2["name"]}: ')
        # end_time_round = Round('')
        # end_time_round.end_time(datetime.now().strftime('%d-%m-%y %H:%M:%S'))
        return score_1, score_2

    @classmethod
    def display_pairings(cls, player_1, player_2):
        # print(f'Nom du round:  {Round("Round 1")}\n\n')
        print(f"Date de début: {datetime.now().strftime('%d-%m-%y %H:%M:%S')}\n")
        # print(f'Date de fin:   {new_round["end"]}\n')
        #
        # i = f'{new_round["matches"][0][0]}, {new_round["matches"][0][0]}'
        print()

        print(
            f' Nom : {player_1["name"]},   Prénom : {player_1["f_name"]} |   Classement :  {player_1["ranking"]}  VS'
            f' Nom : {player_2["name"]}, Prénom : {player_2["f_name"]} | Classement :   {player_2["ranking"]}'
        )

        save_matches = Round("round 1")
        Round.pairing_for_round(save_matches, player_1, player_2)
        # print(match['name'], match['ranking'], match_1['name'], match_1['ranking'])
        # for i in match, match_1:
