class HiddenBox:
    # __BoxName string
    # __Creator string
    # __DateHidden string
    # __GameLocation string
    # __LastFinds[10][2] string
    # __Active bool
    def __init__(self, BN, C, DH, GL):
        self.__BoxName=BN
        self.__Creator=C
        self.__DateHidden=DH
        self.__GameLocation=GL
        self.__Active=False
        self.__LastFinds=[[None for j in range(2)] for i in range(10)]
            
    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


TheBoxes=[HiddenBox(None, None, None, None) for i in range(10000)]

def NewBox():
    NewName=input()
    NewCreator=input()
    NewDateDidden=input()
    NewGameLocation=input()
    TheBoxes.append(HiddenBox(NewName, NewCreator, NewDateHidden, NewGameLocation))

NewBox()

class PuzzleBox(HiddenBox):
    # PuzzleText string
    # Solution string
    def __init__(self, BN, C, DH, GL, PT, S):
        super().__init__(BN, C, DH, GL)
        self.__PuzzleText=PT
        self.__Solution=S
