def Enqueue(NewItem):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer == 50:
        print("The queue is full")
    else:
        Queue.append(NewItem)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("The queue is empty")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


def ReadData():
    try:
        File = open("QueueData.txt", "r")
        ID = File.readline().strip()
        while ID != "":
            Enqueue(ID)
            ID = File.readline().strip()
        File.close()
    except IOError:
        print("File cannot be found")


class RecordData:
    def __init__(self, NewID, NewTotal):
        self.ID = NewID  # string
        self.Total = NewTotal  # integer


def TotalData():
    global Records
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        Flag = True
        NumberRecords += 1
    else:
        for x in range(NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


def OutputRecords():
    global Records
    global NumberRecords
    for i in range(NumberRecords):
        print("ID", Records[i].ID, "Total", Records[i].Total)


Queue = []  # global, string array(list), 50 items
HeadPointer = -1  # global, integer
TailPointer = 0  # global, integer

Records = []  # global, RecordData array(list), 50 items
NumberRecords = 0  # global, integer

ReadData()
for i in range(TailPointer):
    TotalData()
OutputRecords()
