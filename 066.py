N = int(input("Enter N: "))
total =0
for i in range(1,N+1,2):
    total +=i
print("Sum of odd numbers from 1 to ",N,"is",total)