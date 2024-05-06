def IterativeVowels(Value):  # Value is string
    Total = 0
    LengthString = len(Value)
    for i in range(LengthString):
        FirstCharacter = Value[0]
        if (
            FirstCharacter == "a"
            or FirstCharacter == "e"
            or FirstCharacter == "i"
            or FirstCharacter == "o"
            or FirstCharacter == "u"
        ):
            Total += 1
        Value = Value[1 : len(Value)]
    return Total


def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    FirstCharacter = Value[0]
    if (
        FirstCharacter == "a"
        or FirstCharacter == "e"
        or FirstCharacter == "i"
        or FirstCharacter == "o"
        or FirstCharacter == "u"
    ):
        return 1 + RecursiveVowels(Value[1 : len(Value)])
    else:
        return RecursiveVowels(Value[1 : len(Value)])


print(IterativeVowels("house"))

print(RecursiveVowels("imagine"))
