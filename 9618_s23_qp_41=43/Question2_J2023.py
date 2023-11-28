class Vehicle:
    def __init__(self, ID_New, MaxSpeed_New, IncreaseAmount_New):
        self.__ID = ID_New  # string
        self.__MaxSpeed = MaxSpeed_New  # integer
        self.__IncreaseAmount = IncreaseAmount_New  # integer
        self.__CurrentSpeed = 0  # integer
        self.__HorizontalPosition = 0  # integer

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CurrentSpeed_New):
        self.__CurrentSpeed = CurrentSpeed_New

    def SetHorizontalPosition(self, HorizontalPosition_New):
        self.__HorizontalPosition = HorizontalPosition_New

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

    def OutputPosition(self):
        print("Current Position = ", self.__HorizontalPosition)
        print("Current Speed = ", self.__CurrentSpeed)


class Helicopter(Vehicle):
    def __init__(self, ID_New, MaxSpeed_New, IncreaseAmount_New, VerticalChange_New, MaxHeight_New):
        super().__init__(ID_New, MaxSpeed_New, IncreaseAmount_New)
        self.__VerticalChange = VerticalChange_New  # integer
        self.__MaxHeight = MaxHeight_New  # integer
        self.__VerticalPosition = 0  # integer

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().SetCurrentSpeed(super().GetCurrentSpeed() + super().GetIncreaseAmount())
        if super().GetCurrentSpeed() > super().GetMaxSpeed():
            super().SetCurrentSpeed(super().GetMaxSpeed())  # mark scheme added a ';' here. This is python, bro! :)
        super().SetHorizontalPosition(super().GetHorizontalPosition() + super().GetCurrentSpeed())

    def OutputPosition(self):
        super().OutputPosition()
        print("Current Vertical Position = ", self.__VerticalPosition)


Car = Vehicle("Tiger", 100, 20)
Heli = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputPosition()
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.OutputPosition()
