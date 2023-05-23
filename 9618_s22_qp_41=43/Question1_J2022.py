def ReadHighScores():
    global Player
    File = open("HighScore.txt", "r")
    i = 0
    Name = str(File.readline()).strip()
    Score = int(File.readline())
    while Name:
        Player[i][0] = Name
        Player[i][1] = int(Score)
        i += 1
        Name = str(File.readline()).strip()
        Score = File.readline().strip()
    File.close()


def OutputHighScores():
    global Player
    for i in range(10):
        print(Player[i][0], end=" ")
        print(Player[i][1])


def NewList(NewName, NewScore):
    global Player
    PositionFound = False
    i = 0
    Player_Original = [["", None] for k in range(11)]  # a global data structure
    for k in range(11):
        Player_Original[k][0] = str(Player[k][0])
        Player_Original[k][1] = int(Player[k][1])
    while not PositionFound and i <= 9:
        if NewScore >= Player[i][1]:
            PositionFound = True
            Player[i][0] = NewName
            Player[i][1] = NewScore
            for j in range(i, 10, 1):
                print(i, Player_Original)
                Player[j + 1] = Player_Original[j]
        i += 1


def WriteTopTen():
    global Player
    File = open("NewHighScore.txt", "w")
    for i in range(10):
        File.write(Player[i][0] + "\n")
        File.write(str(Player[i][1]) + "\n")
    File.close()


Player = [["", -1] for i in range(11)]  # a global data structure
ReadHighScores()
OutputHighScores()
Name = ""
while len(Name) != 3:
    Name = str(input("Please input a 3-character player name"))
Score = -1
while Score < 1 or Score > 100000:
    try:
        Score = int(input("Please input the integer score between 1 and 100000 inclusive"))
    except ValueError:
        Score = int(input("Please input the integer score between 1 and 100000 inclusive"))
NewList(Name, Score)
OutputHighScores()
WriteTopTen()
