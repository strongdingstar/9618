def PrintArray(DataArray):
    for i in range(len(DataArray)):
        print(DataArray[i], end=' ')
    print("\n")


def LinearSearch(DataArray, SearchValue):
    count = 0
    for i in range(len(DataArray)):
        if DataArray[i] == SearchValue:
            count += 1
    return count


DataArray = [0 for i in range(25)]  # 25 Integer elements

try:
    File = open("Data.txt", "r")
    for i in range(25):
        DataArray[i] = int(File.readline().strip())
    File.close()
except IOError:
    print("The file could not be found")

PrintArray(DataArray)
SearchValue = int(input("enter an integer between 0 and 100 to find"))
while SearchValue < 0 or SearchValue > 100:
    SearchValue = int(input("enter an integer between 0 and 100 to find"))
result = "The number " + str(SearchValue) + " is found " + str(LinearSearch(DataArray, SearchValue)) + " times"
print(result)
