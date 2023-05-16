QueueData=["" for i in range(20)]
StartPointer=0
EndPointer=0

def Enqueue(AddItem):
    global EndPointer
    global QueueData
    if EndPointer>19:
        return False
    else:
        QueueData[EndPointer]=AddItem
        EndPointer+=1
        return True

def ReadFile():
    FileName=input("Please input a filename\n")
    try:
        File=open(FileName, 'r')
        NotFull=True
        InsertData=File.readline()
        while NotFull and InsertData:
            NotFull=Enqueue(InsertData)
            InsertData=File.readline()
        File.close()
        if NotFull:
            return 2
        else:
            return 1
    except OSError:
        return -1

Flag=ReadFile()
if Flag==-1:
    print("the text file could not be found")
elif Flag==1:
    print("the queue was full")
elif Flag==2:
    print("all items were added to the queue")

def Remove():
    global StartPointer
    global EndPointer
    global QueueData
    Item1=QueueData[StartPointer]
    StartPointer+=1
    Item2=QueueData[StartPointer]
    StartPointer+=1
    if Item1 and Item2:
        return Item1+" "+Item2
    else:
        return "No Items"

