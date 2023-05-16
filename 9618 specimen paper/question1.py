TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


def InsertionSort(TheData=[]):
    for Count in range(len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


def OutputData(TheData=[]):
    for Count in range(len(TheData)):
        print(TheData[Count], end=' ')


print("These are the data BEFORE sorting:")
OutputData(TheData)
print('\n')
InsertionSort(TheData)
print("These are the data AFTER sorting:")
OutputData(TheData)


def FindNum():
    WholeNum = int(input())
    ReturnValue = (WholeNum in TheData)
    if ReturnValue:
        print("found")
    else:
        print("not found")
    return ReturnValue


print("\n")
FindNum()
