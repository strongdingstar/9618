def PushData(Letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    Letter = Letter.lower()
    if (
        Letter == "a"
        or Letter == "e"
        or Letter == "i"
        or Letter == "o"
        or Letter == "u"
    ):
        if VowelTop == 100:
            print("The vowel stack is full")
        else:
            StackVowel.append(Letter)
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("The consonant stack is full")
        else:
            StackConsonant.append(Letter)
            ConsonantTop += 1


def ReadData():
    try:
        File = open("StackData.txt", "r")
        for i in range(100):
            PushData(File.readline().strip())
        File.close()
    except IOError:
        print("File cannot be found")


def PopVowel():
    global StackVowel
    global VowelTop
    if VowelTop == 0:
        return "No data"
    VowelTop -= 1
    return StackVowel[VowelTop]


def PopConsonant():
    global StackConsonant
    global ConsonantTop
    if ConsonantTop == 0:
        return "No data"
    ConsonantTop -= 1
    return StackConsonant[ConsonantTop]


StackVowel = []  # global, string array(list), 100 items
StackConsonant = []  # global, string array(list), 100 items

VowelTop = 0  # global, integer
ConsonantTop = 0  # global, integer

ReadData()
Letters = ""
i = 0
while i < 5:
    Choice = input("Pop vowel or consonant?").lower()
    if Choice == "vowel":
        ReturnValue = PopVowel()
        if ReturnValue == "No data":
            print("Vowel stack is empty")
        else:
            Letters += ReturnValue
            i += 1
    elif Choice == "consonant":
        ReturnValue = PopConsonant()
        if ReturnValue == "No data":
            print("Consonant stack is empty")
        else:
            Letters += ReturnValue
            i += 1
print(Letters)
