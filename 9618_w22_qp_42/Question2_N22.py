class Character:
    def __init__(self, Name_new, XCoordinate_new, YCoordinate_new):
        self.__Name = Name_new  # Name as string
        self.__XCoordinate = XCoordinate_new  # XCoordinate as integer
        self.__YCoordinate = YCoordinate_new  # YCoordinate as integer

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):  # BOTH XChange and YChange are integer
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


# Please note that in python, when using "for i in range(10)", the iteration variable i
CharacterArray = []  # CharacterArray as array[0:9] of type Character, it has 10 elements
try:
    File = open("Characters.txt", "r")
    for i in range(10):  # in python, index 10 cannot be reached using "for" iteration
        CharacterArray.append(Character(File.readline().strip(), int(File.readline()), int(File.readline())))
    File.close()
except IOError:
    print("FILE NOT FOUND")
Exists = False  # Exists as boolean(bool)
PositionIndex = -1  # PositionIndex as integer
while not Exists:
    InputName = input("Enter a character's name").strip().lower()  # InputName as string
    for i in range(10):  # in python, index 10 cannot be reached using "for" iteration
        if InputName == str(CharacterArray[i].GetName()).lower():
            PositionIndex = i
            Exists = True
ValidLetter = False
while not ValidLetter:
    letter = input("Enter a letter from A, W, S or D").strip()
    if letter == 'A':
        CharacterArray[PositionIndex].ChangePosition(-1, 0)
        ValidLetter = True
    elif letter == 'W':
        CharacterArray[PositionIndex].ChangePosition(0, 1)
        ValidLetter = True
    elif letter == 'S':
        CharacterArray[PositionIndex].ChangePosition(0, -1)
        ValidLetter = True
    elif letter == "D":
        CharacterArray[PositionIndex].ChangePosition(1, 0)
        ValidLetter = True
print(CharacterArray[PositionIndex].GetName(), "has changed coordinates to X = ", end="")
print(CharacterArray[PositionIndex].GetX(), "and Y = ", end="")
print(CharacterArray[PositionIndex].GetY())
