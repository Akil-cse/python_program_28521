age = int(input("Enter Your age: "))
has_id =input("Do you have ID card?(yes/no): ")
can_enter = (age>=18) and has_id
print("Can enter restricted area(age >=18 AND has id): ",can_enter)
discount = (age<12) or (age>60)
print("Eligible for special discount(age<12 or age>60): ", discount)
print("IS NOT eligible for discount: ", not discount)