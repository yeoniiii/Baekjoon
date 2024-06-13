limit = int(input())
speed = int(input())
over = speed - limit

if over > 0:
    if over <= 20:
        fee = 100
    elif over <= 30:
        fee = 270
    else:
        fee = 500
    print(f"You are speeding and your fine is ${fee}.")
else:
    print("Congratulations, you are within the speed limit!")