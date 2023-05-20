class node:
    def __init__(self, Newdata, NewnextNode=-1):# MARK
        self.data = Newdata
        self.nextNode = NewnextNode


def outputNodes(LinkedList, startPointer1):
    # if (startPointer == -1):
    #     return
    # else:
    #     print(LinkedList[startPointer].data)
    #     outputNodes(LinkedList, LinkedList[startPointer].nextNode)
    while startPointer1 != -1:
        print(LinkedList[startPointer1].data)
        startPointer1 = LinkedList[startPointer1].nextNode


def addNote(LinkedList, startPointer, emptyList):
    addData = input()
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        LinkedList[emptyList] = node(int(addData), -1)
        CurrentPointer = startPointer
        LastPointer = 0
        while CurrentPointer != -1:
            LastPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].nextNode
        LinkedList[LastPointer].nextNode = emptyList
        emptyList = LinkedList[emptyList].nextNode
        return True


LinkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3),
              node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5

outputNodes(LinkedList, startPointer)

Result = addNote(LinkedList, startPointer, emptyList)
if Result:
    print("The data has been successfully added")
else:
    print("There are no empty nodes")
outputNodes(LinkedList, startPointer)
