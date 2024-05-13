class Character:
    def __init__(self, NewName, NewDOB, NewIntel, NewSpeed):
        self.__Name = NewName  # string
        self.__DateOfBirth = NewDOB  # string (date)
        self.__Intelligence = NewIntel  # float (real)
        self.__Speed = NewSpeed  # integer

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__Name

    def SetIntelligence(self, NewIntel):
        self.__Intelligence = NewIntel

    def Learn(self):
        self.__Intelligence *= 1.10

    def ReturnAge(self):
        BirthYear = int(self.__DateOfBirth[-4:])
        return 2023 - BirthYear


class MagicCharacter(Character):
    def __init__(self, NewElement, NewName, NewDOB, NewIntel, NewSpeed):
        super().__init__(NewName, NewDOB, NewIntel, NewSpeed)
        self.__Element = NewElement  # string

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence() * 1.20)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.30)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.10)


FirstCharacter = Character("Royal", "01/01/2019", float(70), 30)

FirstCharacter.Learn()
print(
    FirstCharacter.GetName(),
    "is",
    FirstCharacter.ReturnAge(),
    "years old and has intelligence",
    FirstCharacter.GetIntelligence(),
)

FirstMagic = MagicCharacter("fire", "Light", "03/03/2018", float(75), 22)

FirstMagic.Learn()
print(
    FirstMagic.GetName(),
    "is",
    FirstMagic.ReturnAge(),
    "years old and has intelligence",
    FirstMagic.GetIntelligence(),
)
