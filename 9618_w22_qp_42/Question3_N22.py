def Enqueue(AddValue):  # AddValue as integer
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer > 99:
        return False
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = AddValue
        TailPointer += 1
        return True


def RecursiveOutput(Start):
    global Queue
    global HeadPointer
    global TailPointer
    if Start >= HeadPointer:
        return Queue[Start] + RecursiveOutput(Start - 1)
    else:
        return 0


Queue = [-1 for i in range(100)]  # Queue as array[0:99] of integer, it has 100 elements
HeadPointer = -1
TailPointer = 0
Success = True
for i in range(1, 21, 1):
    ReturnValue = Enqueue(i)
    if ReturnValue == False:
        Success = False
if Success:
    print("Successful")
else:
    print("Unsuccessful")
print(RecursiveOutput(TailPointer - 1))
