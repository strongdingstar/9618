def ReadFile():
    global DataArray
    try:
        FILE = open("IntegerData.txt", "r")
        for i in range(100):
            DataArray[i] = int(FILE.readline().strip())
    except IOError:
        print("The file could not be found")


def FindValues():
    UserNumber = 0
    while UserNumber < 1 or UserNumber > 100:
        UserNumber = int(input("Enter a number to search between 1 and 100"))
    appearance = 0
    for i in range(100):
        if DataArray[i] == UserNumber:
            appearance += 1
    return appearance


def BubbleSort():
    global DataArray
    i = 0
    Flag = True
    while i < 100 and Flag is True:
        Flag = False
        for j in range(0, 100 - i - 1, 1):
            if DataArray[j] > DataArray[j + 1]:
                Flag = True
                Temp = DataArray[j]
                DataArray[j] = DataArray[j + 1]
                DataArray[j + 1] = Temp
        i += 1
    for k in range(100):
        print(DataArray[k])


DataArray = [0 for i in range(100)]
ReadFile()
print("This number appeared", FindValues(), "times in the data")
BubbleSort()
