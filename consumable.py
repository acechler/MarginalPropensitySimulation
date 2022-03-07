



#
#       A Consumable is an object that has a name and has value.
#    A Consumable will have value TODO = and be sold between entities
#
class Consumable(object):
    __name = ""
    __value = 0

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def info(self):
        print(self.__name + " is worth $", self.__value)

    @property
    def get_name(self):
        return self.__name

    @property
    def get_value(self):
        return self.__value
