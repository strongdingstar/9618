import random


def OutputValues():
    global ArrayData
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], end=' ')
        print('\n')


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = int((Lower + Upper - 1) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    else:
        return -1


ArrayData = [[random.randint(1, 100) for i in range(10)] for j in range(10)]
print("These are the values before sorting")
OutputValues()
ArrayLength = 10
for X in range(ArrayLength):
    for Y in range(ArrayLength - 1):
        for Z in range(ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z + 1]
                ArrayData[X][Z + 1] = TempValue
print("These are the values after sorting")
OutputValues()
InputSearchValue = int(input("Input SearchValue 1").strip())
print(BinarySearch(ArrayData, 0, ArrayLength, InputSearchValue))
InputSearchValue = int(input("Input SearchValue 2").strip())
print(BinarySearch(ArrayData, 0, ArrayLength, InputSearchValue))