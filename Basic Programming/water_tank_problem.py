h = 10
r = 5
F = 15
t = int(input('Enter the time '))

Vtank = 3.14 * r ** 2 * h
Vwtr = F * t

if Vtank < Vwtr:
    print("Overflow Condition")
    print("Overflow Volume", Vwtr - Vtank)
elif Vtank == Vwtr:
    print("Tank is full ")
else:
    print("Underflow condition ")
    ht = Vwtr / (3.14 * r ** 2)
    hr = h - ht
    print("Filled Height", ht)
    print("Remaining Height", hr)
    
    
