target = 1000
sales = int(input("Enter sales: "))
if sales < target:
    bonus = 100
    print("Total wage = ", sales + bonus)
elif sales > target:
    bonus = 200
    print("Total wage = ", sales + bonus)
else:
    print("There is no bonus for this worker.")