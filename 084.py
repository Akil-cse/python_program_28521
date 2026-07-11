num = int(input("Enter a number: "))
temp = num 
rev_num = 0
while temp>0:
    digit = temp%10
    rev_num = (rev_num*10)+digit
    temp = temp//10
if rev_num == num:
    print(num,"is a Palindrome number")
else:
    print(num,"is NOT a Palindrome number")
