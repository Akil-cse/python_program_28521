chocolates =int(input(" Enter total Chocolates"))
children = int(input("Enter number of children"))
per_chid =chocolates//children
remaining = chocolates%children
print("Each child gets:",per_chid,"Chocolates")
print("Chocolates left:",remaining)