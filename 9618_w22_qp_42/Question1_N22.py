def Initialise():
    global Jobs
    global NumberOfJobs
    Jobs = [[-1, -1] for i in range(100)]
    NumberOfJobs = 0


def AddJob(JobNumber, JobPriority):  # both JobNumber and JobPriority are integer
    global Jobs
    global NumberOfJobs
    if NumberOfJobs >= 100:
        print("Not Added")
    else:
        Jobs[NumberOfJobs][0] = int(JobNumber)
        Jobs[NumberOfJobs][1] = int(JobPriority)
        NumberOfJobs += 1
        print("Added")


def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        Temp = Jobs[i]
        j = i
        while j > 0 and Temp[1] < Jobs[j - 1][1]:
            Jobs[j] = Jobs[j - 1]
            j -= 1
        Jobs[j] = Temp


def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(Jobs[i][0], " priority ", Jobs[i][1])


Jobs = [[]]  # global array of integer, 100 by 2 elements
NumberOfJobs = 0  # global integer
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()
