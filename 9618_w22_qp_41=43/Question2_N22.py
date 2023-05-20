class Card:
    def __init__(self, newNumber, newColour):
        self.__Number = newNumber  # Number - integer (int)
        self.__Colour = newColour  # Colour - string (str)

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):  # all Card parameters have type Card (Card)
        self.__Cards = []  # Cards - list(array) of type Card (Card)
        self.__Cards.append(Card1)  # type Card (card)
        self.__Cards.append(Card2)  # type Card (card)
        self.__Cards.append(Card3)  # type Card (card)
        self.__Cards.append(Card4)  # type Card (card)
        self.__Cards.append(Card5)  # type Card (card)
        self.__Cards.append(Card(0, ""))  # type Card (card)
        self.__Cards.append(Card(0, ""))  # type Card (card)
        self.__Cards.append(Card(0, ""))  # type Card (card)
        self.__Cards.append(Card(0, ""))  # type Card (card)
        self.__Cards.append(Card(0, ""))  # type Card (card)
        self.__FirstCard = 0  # FirstCard - integer (int)
        self.__NumberCards = 5  # NumberCards - integer (int)

    def GetCard(self, index):
        return self.__Cards[index]


def CalculateValue(PlayerHand):
    score = 0
    for i in range(10):
        TempCard = PlayerHand.GetCard(i)
        if TempCard.GetColour() == "red":
            score += 5
        elif TempCard.GetColour() == "blue":
            score += 10
        elif TempCard.GetColour() == "yellow":
            score += 15
        score += TempCard.GetNumber()
    return score


OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)
Score1 = CalculateValue(Player1)
Score2 = CalculateValue(Player2)
if Score1 > Score2:
    print("Player1 wins")
elif Score2 > Score1:
    print("Player2 wins")
elif Score1 == Score2:
    print("draw")
