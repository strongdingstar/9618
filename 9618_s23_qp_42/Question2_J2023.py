class SaleData:
    def __init__(self, NewID, NewQuantity):
        self.ID = NewID  # string
        self.Quantity = NewQuantity  # integer


def Enqueue(NewRecord):
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        if Tail == 4:
            Tail = 0
        else:
            Tail += 1
        NumberOfItems += 1
        return 1


def Dequeue():
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    if Head == 4:
        Head = 0
    else:
        Head += 1
    NumberOfItems -= 1
    return CircularQueue[Head - 1]


def EnterRecord():
    ReturnValue = Enqueue(SaleData(input("Enter ID"), input("Enter quantity")))
    if ReturnValue == -1:
        print("Full")
    else:
        print("Stored")


CircularQueue = [SaleData("", -1) for i in range(5)]  # SaleData array(list), 5 elements
Head = 0  # global, integer
Tail = 0  # global, integer
NumberOfItems = 0  # global, integer

for i in range(6):
    EnterRecord()
ReturnValue = Dequeue()
if ReturnValue == SaleData("", -1):
    print("error: empty items")
else:
    print(ReturnValue.ID, " ", ReturnValue.Quantity)
EnterRecord()
for i in range(5):
    print(CircularQueue[i].ID, " ", CircularQueue[i].Quantity)
