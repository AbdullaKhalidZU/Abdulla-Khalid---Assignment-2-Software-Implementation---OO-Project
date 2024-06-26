# -*- coding: utf-8 -*-
"""Visitor class

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U1V2TOc9WbOagSHAtgwEDmNHLRwpS663
"""

class Visitor:
    def __init__(self, name, age, national_id, ticket_type):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.ticket_type = ticket_type

    # Getter and setter methods for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter methods for age
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # Getter and setter methods for national_id
    def get_national_id(self):
        return self.national_id

    def set_national_id(self, national_id):
        self.national_id = national_id

    # Getter and setter methods for ticket_type
    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type