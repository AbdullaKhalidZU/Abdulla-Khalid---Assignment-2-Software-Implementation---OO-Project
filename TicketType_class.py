# -*- coding: utf-8 -*-
"""TicketType   class

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jh1IYP-e932aI4-LbgSDPEYI9AFHy_KC
"""

class TicketType:
    def __init__(self, type, base_price, is_free, discount_percentage):
        self.type = type
        self.base_price = base_price
        self.is_free = is_free
        self.discount_percentage = discount_percentage

    # Getter and setter methods for type
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    # Getter and setter methods for base_price
    def get_base_price(self):
        return self.base_price

    def set_base_price(self, base_price):
        self.base_price = base_price

    # Getter and setter methods for is_free
    def is_free(self):
        return self.is_free

    def set_free(self, is_free):
        self.is_free = is_free

    # Getter and setter methods for discount_percentage
    def get_discount_percentage(self):
        return self.discount_percentage

    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage