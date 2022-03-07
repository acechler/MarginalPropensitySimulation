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
from entity import *
from consumable import *

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

# Run a basic test that initializes an apple item
def consumable_test():
    apple = Consumable(name='apple', value=2.00)
    apple.info()

if __name__ == '__main__':
    entity_test()
    consumable_test()
