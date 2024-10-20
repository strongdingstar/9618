class Character:
    def __init__(self, NewName, NewXP, NewYP):
        self.__Name = NewName  # string
        self.__XPosition = NewXP  # integer
        self.__YPosition = NewYP  # integer

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, XAdd):
        self.__XPosition += XAdd
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, YAdd):
        self.__YPosition += YAdd
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(10)
        elif Direction == "down":
            self.SetYPosition(-10)
        elif Direction == "left":
            self.SetXPosition(-10)
        elif Direction == "right":
            self.SetXPosition(10)


class BikeCharacter(Character):
    # NewName, string
    # NewXP, integer
    # NewYP, integer
    def __init__(self, NewName, NewXP, NewYP):
        super().__init__(NewName, NewXP, NewYP)

    def Move(self, Direction):
        if Direction == "up":
            super().SetYPosition(20)
        elif Direction == "down":
            super().SetYPosition(-20)
        elif Direction == "left":
            super().SetXPosition(-20)
        elif Direction == "right":
            super().SetXPosition(20)


Jack = Character("Jack", 50, 50)

Karla = BikeCharacter("Karla", 100, 50)

CharacterInput = input("Move Jack or Karla?").lower()
while CharacterInput != "jack" and CharacterInput != "karla":
    CharacterInput = input("Invalid input, please try again").lower()
DirectionInput = input("Move in which direction? up, down, left, or right?").lower()
while (
    DirectionInput != "up"
    and DirectionInput != "down"
    and DirectionInput != "left"
    and DirectionInput != "right"
):
    DirectionInput = input("Invalid input, please try again").lower()
if CharacterInput == "jack":
    Jack.Move(DirectionInput)
    print("Jack's new position is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
else:
    Karla.Move(DirectionInput)
    print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())
