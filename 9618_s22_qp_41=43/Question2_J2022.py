class Balloon:
    def __init__(self, NewColour, NewDefenceItem):
        self.__Colour = NewColour  # Colour is a string(str)
        self.__DefenceItem = NewDefenceItem  # DefenceItem is a string(str)
        self.__Health = 100  # Health is an integer(int)

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, AddHealth):
        self.__Health += int(AddHealth)

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False


def Defend(BalloonObject):
    OpponentStrength = input("Enter the strength of an opponent")
    BalloonObject.ChangeHealth(OpponentStrength)
    print("Used", BalloonObject.GetDefenceItem(), "to defence")
    Flag = BalloonObject.CheckHealth()
    if Flag:
        print("There is NO health remaining")
    else:
        print("There is health remaining")
    return BalloonObject


DefenceItem1 = input("Enter the DefenceItem")
Colour1 = input("Enter the Colour")
Balloon1 = Balloon(Colour1, DefenceItem1)
Balloon1 = Defend(Balloon1)
