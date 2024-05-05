def SortDescending():
    ArrayLength = len(Animals)
    Temp = ""
    for x in range(ArrayLength - 1):
        for y in range(ArrayLength - x - 1):
            if Animals[y][:1] < Animals[y + 1][:1]:
                Temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = Temp


global Animals  # string array(list) with 10 elements

Animals = []
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

SortDescending()
for i in range(len(Animals)):
    print(Animals[i])
