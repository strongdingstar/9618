def linearSearch(SearchValue):  # SearchValue must be an integer
    SearchValue = int(SearchValue)
    global arrayData
    if SearchValue in arrayData:
        return True
    else:
        return False


def bubbleSort():
    global arrayData
    temp = None
    for x in range(0, len(arrayData) - 1):
        for y in range(0, len(arrayData) - x - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
IntegerValue = int(input())  # IntegerValue must be an integer
flag = linearSearch(IntegerValue)
if flag:
    print("The value was found")
else:
    print("The value was NOT found")
