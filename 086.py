num = int(input("Enter a number: "))
square = num**2
temp = square
sum_digit = 0 
while temp>0:
    digit = temp%10
    sum_digit += digit
    temp = temp//10
if sum_digit == num:
    print(num,"is a Neon number")
else:
    print(num,"is NOT a Neon number" )