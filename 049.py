a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a<b and a<c:
    print("Smallest number is: ",a)
elif b<a and b<c:
    print("Smallest number is: ",b)
else:
    print("Smallest number is: ",c)
