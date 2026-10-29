num = 7
won = False

for attempt in range(7):
    
    try:
        guess = int(input("Guess a number? "))
    except ValueError:
        print("Please enter a whole number.")
        continue


    if guess == num:
        print("Correct!")
        won = True
        break
    elif guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    
if won == False:
    print("Game over")