num = int(input("Enter a positive integer: "))
if num<=0:
    print("Please a positive number greater than 0")
else:
    sum_divisors = 0
    for i in range(1,(num//2)+1):
        if num%i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(num,"is a perfect number")
    else:
        print(num,"is NOT a perfect number")
