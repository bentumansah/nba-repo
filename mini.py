x = float(input("Enter the first operand: "))

y = float(input("Enter the second operand: "))

print("""1. Add
2. Subtract
3. Multiply
4. Divide""")

mathematical_operator = int(input("Enter the operator: "))

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