def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    print("Enter the data")
    NodeData = int(input())
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")


def PrintAll():
    for i in range(20):
        for j in range(3):
            print(ArrayNodes[i][j], end=' ')
        print("\n")


def InOrder(index):
    if ArrayNodes[index][0] != -1:
        InOrder(ArrayNodes[index][0])
    print(ArrayNodes[index][1])
    if ArrayNodes[index][2] != -1:
        InOrder(ArrayNodes[index][2])
    return


ArrayNodes = [[-1, None, -1] for i in range(20)]
RootPointer = -1
FreeNode = 0

for k in range(10):
    AddNode()
    # PrintAll()

InOrder(0)
