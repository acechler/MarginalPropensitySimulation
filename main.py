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


# Run a basic test between two entities
def entity_test():
    salesmen = Entity(name="Salesmen", money=0)
    merchant = Entity(name="Merchant", money=0)

    salesmen.add_money(100)
    salesmen.show_money()
    salesmen.give_money(merchant)
    merchant.show_money()
    merchant.give_money(salesmen)
    salesmen.show_money()
    merchant.show_money()


if __name__ == '__main__':
    entity_test()
