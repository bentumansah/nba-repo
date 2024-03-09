def family():
    papa = [11, 12, 13, 14, 15, 16]
    son = [6, 7, 8, 9, 10]
    print(papa, son)
    print(papa.insert(0, [0, 1, 2, 3, 4, 5]))
    



family()
x = float(input("Enter the first number: "))

y = float(input("Enter the second number: "))

print("""1. Add
2. Subtract
3. Multiply
4. Divide""")

mathematical_operator = input("Enter the operator: ")

if mathematical_operator == 1:
    print(f"The sum of the operands is {x + y}")
elif mathematical_operator == 2:
    print(f"The difference between the operands is {x - y}")
elif mathematical_operator == 3:
    print(f"The product of the operands is {x * y}")
elif mathematical_operator == 4:
    print(f"The quotient of the operands is {x / y}")
else:
    print("Invalid operation")