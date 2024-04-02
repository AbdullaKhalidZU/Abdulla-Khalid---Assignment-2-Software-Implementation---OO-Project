# -*- coding: utf-8 -*-
"""Artwork Class

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fBVlby7n3PZMlvpFHU_0p73YNzm9fk5p
"""

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance

    # Getter and setter methods for title
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    # Getter and setter methods for artist
    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    # Getter and setter methods for date_of_creation
    def get_date_of_creation(self):
        return self.date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    # Getter and setter methods for historical_significance
    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance