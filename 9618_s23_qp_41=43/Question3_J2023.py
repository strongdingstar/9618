def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global Animal
    global AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush):
    global Colour
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True


def PopColour():
    global Colour
    global ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def ReadData():
    try:
        global Animal
        global AnimalTopPointer
        File = open("AnimalData.txt", "r")
        line = File.readline().strip()
        while line != "":
            PushAnimal(line)
            line = File.readline().strip()
        File.close()
        global Colour
        global ColourTopPointer
        File = open("ColourData.txt", "r")
        line = File.readline().strip()
        while line != "":
            PushColour(line)
            line = File.readline().strip()
        File.close()
    except IOError:
        print("The file could not be found")


def OutputItem():
    A_Return = PopAnimal()
    C_Return = PopColour()
    if C_Return == "":
        PushAnimal(A_Return)
        print("No colour")
    else:
        if A_Return == "":
            PushColour(C_Return)
            print("No animal")
        else:
            print(C_Return, A_Return)


Animal = ["" for i in range(20)]  # 20 string elements
Colour = ["" for i in range(10)]  # 10 string elements
AnimalTopPointer = 0  # integer
ColourTopPointer = 0  # integer
ReadData()
for i in range(4):
    OutputItem()
