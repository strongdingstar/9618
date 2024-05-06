"""
Plese note that the mark scheme screenshot for Question 3 is likely to be wrong
Tested by running the mark scheme's code, the screenshot should look like this:
12452
   730.5600000000001
21548
   890.0
02586
   674.915625
65912
   475.0
42004
   768.5955
82610
   502.075
51947
   1216.1408999999999
51847
   339.5925
"""


class Employee:
    def __init__(self, NewHrPay, NewEmployeeNum, NewJobTitle):
        self.__HourlyPay = NewHrPay  # float
        self.__EmployeeNumber = NewEmployeeNum  # string
        self.__JobTitle = NewJobTitle  # string
        self.__PayYear2022 = [0.0 for i in range(52)]  # array, 52 float elements

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, Week, Hours):
        self.__PayYear2022[Week - 1] = self.__HourlyPay * Hours

    def GetTotalPay(self):
        TotalPay = 0
        for i in self.__PayYear2022:
            TotalPay += i
        return TotalPay


class Manager(Employee):
    def __init__(self, NewBonusVal, NewHrPay, NewEmployeeNum, NewJobTitle):
        super().__init__(NewHrPay, NewEmployeeNum, NewJobTitle)
        self.__BonusValue = NewBonusVal  # float

    def SetPay(self, Week, Hours):
        Hours *= (self.__BonusValue + 100) / 100
        super().SetPay(Week, Hours)


def EnterHours():
    global EmployeeArray
    try:
        File = open("HoursWeek1.txt", "r")
        for x in range(8):
            Num = File.readline().strip()
            Hours = float(File.readline().strip())
            for i in range(8):
                if EmployeeArray[i].GetEmployeeNumber() == Num:
                    EmployeeArray[i].SetPay(1, Hours)
        File.close()
    except IOError:
        print("File cannot be found")


EmployeeArray = []  # array, 8 Employee or Manager elements
try:
    File = open("Employees.txt", "r")
    for i in range(8):
        Pay = float(File.readline().strip())
        Num = File.readline().strip()
        Temp = File.readline().strip()
        try:
            Bonus = float(Temp)
            Job = File.readline().strip()
            EmployeeArray.append(Manager(Bonus, Pay, Num, Job))
        except ValueError:
            Job = Temp
            EmployeeArray.append(Employee(Pay, Num, Job))
    File.close()
except IOError:
    print("File cannot be found")
EnterHours()
for i in range(8):
    print(EmployeeArray[i].GetEmployeeNumber(), EmployeeArray[i].GetTotalPay())
