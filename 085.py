num = int(input("Enter a number: "))
square = num**2
# Check if square ends with the original number
if str(square).endswith(str(num)):
    print(num,"is an Automorphic number (Square:",square,")")
else:
    print(num,"is NOT an Automorphic number(Square:",square,")")