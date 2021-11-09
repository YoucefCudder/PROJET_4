#!/usr/bin/python3
# coding: utf8
from ..vues.vue import ViewMenu, UsefulView
from ..modeles.modele_player import Player
from ..vues.vue_player import PlayerView


class PlayersControl:
    """
    doctstring
    """

    def __init__(self):
        self.view_player = PlayerView()
        self.menu = ViewMenu(menu=None)
        self.vue = UsefulView()

    def select_players(self, players_total):

        players = Player.deserialize_players()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i].doc_id)

        tour_players = []

        i = 0
        while i < players_total:
            self.view_player.select_players(players, i + 1)
            self.vue.input_prompt()
            user_input = input()

            if user_input == "back":
                self.menu.display_menu()

            elif not user_input.isdigit():
                self.vue.input_error()

            elif int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1
            else:
                self.view_player.player_already_selected()

        return tour_players
