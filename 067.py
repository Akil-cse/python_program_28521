N = int(input("Enter N: "))
total = 0
for i in range(5,N+1,5):
    total +=i
print("Sum of numbers divisible by 5 up to", N,"is",total)