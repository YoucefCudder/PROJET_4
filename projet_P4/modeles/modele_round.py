#!/usr/bin/python3
# coding: utf8
from datetime import datetime


class Round:
    def __init__(self, round_name):
        self.round_name = round_name
        self.start_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        self.end_time = None
        self.matches = []

    def round_info(self):
        return [
            self.round_name,
            self.start_time,
            self.end_time,
            self.matches
        ]


