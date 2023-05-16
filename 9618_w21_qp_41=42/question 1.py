def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return int(Unknown(X + 1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return Unknown(X - 1, Y) // 2


def IterativeUnknown(X, Y):
    output_value = X + Y
    ans = 1
    if X < Y:
        for i in range(Y - X):
            print(output_value)
            ans *= 2
            output_value += 1
    elif X == Y:
        ans = 1
    elif X > Y:
        for i in range(X - Y):
            print(output_value)
            ans //= 2
            output_value -= 1
    return ans

print("parameters:", 10, 15)
print("return value:", Unknown(10, 15))
print("parameters:", 10, 10)
print("return value:", Unknown(10, 10))
print("parameters:", 15, 10)
print("return value:", Unknown(15, 10))

print("parameters:", 10, 15)
print("return value:", IterativeUnknown(10, 15))
print("parameters:", 10, 10)
print("return value:", IterativeUnknown(10, 10))
print("parameters:", 15, 10)
print("return value:", IterativeUnknown(15, 10))
