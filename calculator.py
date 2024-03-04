#This simple calculator project accepts only float and integer inputs.
x = float(input("Enter the first number: "))

y = float(input("Enter the second number: "))

print("""1. Add
2. Subtract
3. Multiply
4. Divide""") #Select an operation to perform

mathematical_operation = int(input("Enter an operator: "))

#Allow the user to input an option for the operation to be used

if mathematical_operation == 1:
    print(f"The sum of your inputs is {x + y}")
    # We code for additon using formatted string
elif mathematical_operation == 2:
    print(f"The difference between your inputs is: {x - y}")
    # We code for subtraction using formatted string
elif mathematical_operation == 3:
      print(f"The product of your inputs is: {x * y}")
    # We code for multiplication using formatted sring
elif mathematical_operation == 4:
      print(f"The quotient of your inputs is: {x / y}")
    # We code for division using formatted string
else:
    print("Invalid Input")
    # User's input cannot be interpreted.