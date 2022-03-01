###
# This simulates the Macroeconomic concept known as Marginal Propensity to Save/Consume.
# MPS/MPC is used to simulate a consumers need to save and spend money.
#
#   Example
#       MPC = 0.6
#       MPS = 0.4
#       MPC + MPS = 1
#
#       Consumer has $20
#       They will consume $20 * MPC(0.6) = $12
#       They will save $20 * MPS(0.4) = $8
#       12 + 8 = 20
#


MPS = 0.4
MPC = 0.6


##
#       Entity is an object that has a name and has money.
#    Entity can receive money and give money to another Entity
#
class Entity(object):
    __name = ""
    __money = 0

    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    def add_money(self, amt):
        self.__money += amt
        print(self.__name + " has been given $", amt)

    def show_money(self):
        print(self.__name + " has $", self.__money)

    def give_money(self, entity):
        amt = self.__money * MPC
        entity.add_money(amt)
        self.__money -= amt


if __name__ == '__main__':
    salesmen = Entity(name="Salesmen", money=0)
    merchant = Entity(name="Merchant", money=0)

    salesmen.add_money(100)
    salesmen.show_money()
    salesmen.give_money(merchant)
    merchant.show_money()
    merchant.give_money(salesmen)
    salesmen.show_money()
    merchant.show_money()

