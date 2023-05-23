class Card:
    def __init__(self, NewNumber, NewColour):
        self.__Number = NewNumber  # Number is integer (int)
        self.__Colour = NewColour  # Colour is string (str)

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


def ChooseCard():
    global Selected
    InputIndex = 0
    while InputIndex < 1 or InputIndex > 30:
        InputIndex = int(input("Enter an index from 1 to 30 inclusive"))
    InputIndex = InputIndex - 1
    while Selected[InputIndex]:
        print("The card has already been selected")
        InputIndex = int(input("Enter an index from 1 to 30 inclusive"))
        InputIndex = InputIndex - 1
    print("valid card")
    Selected[InputIndex] = True
    return InputIndex


CardData = [Card(-1, "") for i in range(30)] #type Card
try:
    File = open("CardValues.txt", "r")
    for i in range(30):
        NewCard = Card(int(File.readline().strip()), str(File.readline().strip()))
        CardData[i] = NewCard
    File.close()
except IOError:
    print("THE FILE CANNOT BE FOUND")
Selected = [False for i in range(30)]
Player1 = [] #type Card
for i in range(4):
    Player1.append(CardData[ChooseCard()])
for i in range(4):
    print("number:", Player1[i].GetNumber(), " colour:", Player1[i].GetColour())
