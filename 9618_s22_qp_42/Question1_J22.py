def OutputStack():
    global StackData
    global StackPointer
    print("10 elements in stack:")
    for i in range(10):
        print(StackData[i])
    print("StackPointer is:")
    print(StackPointer)


def Push(AddInt):
    global StackData
    global StackPointer
    if StackPointer < 10:
        StackData[StackPointer] = AddInt
        StackPointer += 1
        return True
    else:
        return False


def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnValue = StackData[StackPointer - 1]
        StackPointer -= 1
        return ReturnValue


StackData = [-1 for i in range(10)]
StackPointer = 0
for i in range(11):
    UserNumber = int(input("please input a number").strip())
    AddSuccess = Push(UserNumber)
    if AddSuccess:
        print("the number is added to stack")
    else:
        print("the number is not added since stack is full")
OutputStack()
Pop()
Pop()
OutputStack()
