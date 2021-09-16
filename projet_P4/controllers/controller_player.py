#!/usr/bin/python3
# coding: utf8

from ..vues.vue import MenuVue
from ..vues.vue_player import VuePlayer


class PlayersControl:
    """
    doctstring
    """

    def __call__(self, *args, **kwargs):
        return PlayersControl.create_players

    def create_players(self, f_name, name):
        """ Input for create player & return inputs """

        VuePlayer().create_player_input()
        MenuVue.display_end_message(f_name, name)





# def sorted_rank(self):
# sorted_players = sorted(self.players, key=itemgetter("ranking"))
# return sorted_players
# nouveau_joueur = PlayersControl().create_players()
# Player(f_name=nouveau_joueur['f_name'], name=nouveau_joueur['name'], gender=nouveau_joueur['gender'],
# birthdate=nouveau_joueur['birthdate'], age=nouveau_joueur['age'], score=nouveau_joueur['score'],
# ranking=nouveau_joueur['ranking']).create_players()
