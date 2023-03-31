def countA(w):
    numA = 0
    for i in range(0, len(w)):
        if w[i] == "a":
            numA = numA + 1
    return numA