import random, time

def guess_the_number(x):
    random_num = random.randint(1,x)
    your_num = 0
    i = 0

    while your_num != random_num:
        your_num = int(input(f"Pick random number between 1 and {x}:"))
        i = i + 1

        if your_num < random_num:
            print("You are kinda wrong, higher")
        elif your_num > random_num:
            print("You are kinda wrong, lower")

    print("You won, great job and also u are beatiful :D")
    time.sleep(1.5)
    print("It takes u", i, "attempts")
    

guess_the_number(random.randint(2,25))
time.sleep(2)
