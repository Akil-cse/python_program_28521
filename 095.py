N = int(input("Enter N: "))
fact = 1
print("Factorial series up to",N,":")
for i in range(1,N+1):
    fact *= i
    print(f"{i}! = {fact}") #f string
    # print(i,"! = ", fact)
