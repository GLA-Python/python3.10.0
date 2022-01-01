def armstrong(x):
    x = str(x)
    ln = len(x)
    sm = 0
    for i in x:
        sm += int(i) ** ln

    return sm == int(x)

def perfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s == x   