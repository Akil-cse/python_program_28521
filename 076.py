N = int(input("Enter fibonacci term you want (N): "))
if N < 0:
    print("Please enter a positive integer greater than 0")
elif N == 1:
    print("The 1st fibonacci number is : 0 ")
elif N == 2:
    print("The 2nd fibonacci number is : 1")

else:
    a,b=0,1
    for i in range(3,N+1):
        c= a+b
        a,b= b,c
    print("The",N,"th fibonacci is:",b)
