class Picture:
    def __init__(self, NewDescription, NewWidth, NewHeight, NewFrameColour):
        self.__Description = NewDescription  # string(str)
        self.__Width = NewWidth  # integer(int)
        self.__Height = NewHeight  # integer(int)
        self.__Framecolour = (str(NewFrameColour)).lower()  # string(str)

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetFrameColour(self):
        return self.__Framecolour

    def SetDescription(self, NewDescription):
        self.__Description = NewDescription


def ReadData():
    global PictureArray
    Count = 0
    try:
        File = open("Pictures.txt", "r")
        Description = File.readline().strip()
        while Description:
            Width = int(File.readline().strip())
            Height = int(File.readline().strip())
            FrameColour = File.readline().strip()
            PictureArray[Count] = Picture(Description, Width, Height, FrameColour)
            Description = File.readline().strip()
            Count += 1
    except OSError:
        print('The File can NOT be found')
    return Count


PictureArray = [Picture("", 0, 0, "") for i in range(100)]

ReadData()

UserColour = str(input()).strip().lower()
MaxWidth = int(input())
MaxHeight = int(input())
for i in range(100):
    if PictureArray[i].GetFrameColour() == UserColour and PictureArray[i].GetWidth() <= MaxWidth and PictureArray[i].GetHeight() <= MaxHeight:
        print(PictureArray[i].GetDescription(),end=' ')
        print(PictureArray[i].GetWidth(), end=' ')
        print(PictureArray[i].GetHeight())
