from item import *

# Marginal Propensity
MPS = 0.4
MPC = 0.6


#
#       Entity is an object that has a name and has money.
#    Entity can receive money and give money to another Entity
#    TODO = Entities will also have an inventory of items.
#
class Entity(object):
    __name = ""
    __money = 0
    __current_items = []

    def __init__(self, name, money):
        self.__name = name
        self.__money = money
        self.__current_items = []

    # Getters
    @property
    def get_name(self):
        return self.__name

    @property
    def get_money(self):
        return self.__money

    # Give entity money.
    def add_money(self, amt):
        self.__money += amt
        print(self.__name + " has been given $", amt)

    # Show how much money an entity has.
    def show_money(self):
        print(self.__name + " has $", self.__money)

    # Have an entity give money to another entity.
    def give_money(self, entity):
        amt = self.__money * MPC
        entity.add_money(amt)
        self.__money -= amt
