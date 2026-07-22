N= int(input("Enter N:"))
total = 0
for i in range(2,N+1,2):
    total+= i**2
print("Sum of even square series is:",total)
