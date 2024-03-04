secret_number = 7
guess_number = 0
guess_limit = 4
while guess_number < guess_limit:
    guess = int(input('Guess: '))
    guess_number += 1
    if guess == secret_number:
        print("""You made the right guess. 
You won!""")
        break
else:
    print("Sorry, you failed!")