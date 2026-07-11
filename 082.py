num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
total_sum = 0
temp = num
while temp>0:
    digit = temp%10
    total_sum += digit**power
    temp = temp // 10
if total_sum ==num:
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT an Armstrong number")


