def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems == 10:
        return False
    else:
        QueueArray[TailPointer] = DataToAdd
        if TailPointer >= 9:
            TailPointer = 0
        else:
            TailPointer += 1
        NumberItems += 1
        return True


def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems == 0:
        return "FALSE"
    else:
        returnvalue = QueueArray[HeadPointer]
        QueueArray[HeadPointer] = "0"
        if HeadPointer >= 9:
            HeadPointer = 0
        else:
            HeadPointer+=1
        NumberItems -= 1
        return returnvalue


QueueArray = ["0" for i in range(10)]
HeadPointer = 0
TailPointer = 0
NumberItems = 0
for i in range(11):
    SuccessfulFlag = Enqueue(input().strip())
    if SuccessfulFlag:
        print("The addition was successful")
    else:
        print("The addition was NOT successful")
print(Dequeue())
print(Dequeue())
