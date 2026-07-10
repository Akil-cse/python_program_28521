a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print(" Valid Triangle ! A triangle CAN be formed")
else:
    print("Invalid Triangle ! A triangle CAN NOT be formed")

