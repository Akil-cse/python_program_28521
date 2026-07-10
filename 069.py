N = int(input("Enter N:"))
print("Numbers divisible bu both 3 and 5 up to",N,"are:")
for i in range(1,N+1,1):
    if i%3 == 0 and i%5 == 0 :
        print(i,end=",")