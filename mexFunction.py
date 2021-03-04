def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found


print(mexFunction([0, 4, 2, 3, 1, 7], 10))


