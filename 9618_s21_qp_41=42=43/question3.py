class TreasureChest:
    # question string(str)
    # answer integer(int)
    # points integer(int)
    def __init__(self, Newquestion, Newanswer, Newpoints):
        self.__question = str(Newquestion)
        self.__answer = int(Newanswer)
        self.__points = int(Newpoints)

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, Useranswer):
        if Useranswer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0


def readData():
    try:
        File = open("TreasureChestData.txt", "r")
        global arrayTreasure
        arrayTreasure = []
        for i in range(5):
            Newquestion = File.readline().strip()
            Newanswer = int(File.readline().strip())
            Newpoints = int(File.readline().strip())
            arrayTreasure.append(TreasureChest(Newquestion, Newanswer, Newpoints))
        File.close()
    except OSError:
        print("The file is NOT found")


readData()
QuestionNum = int(input("Enter a question number between 1 and 5\n")) - 1
StopAsking = False
Count = 0
while not StopAsking:
    print(arrayTreasure[QuestionNum].getQuestion())
    answer = int(input())
    Count += 1
    if arrayTreasure[QuestionNum].checkAnswer(answer):
        StopAsking = True
print(arrayTreasure[QuestionNum].getPoints(Count))
