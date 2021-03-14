import random, time

my_num = input("Pick number,which the pc will be guessing(1-100):")

def computer_guessing(x):
    low = 1
    high = x
    pc_number = random.randint(low,high)
    result = ""

    while result != "C":
        pc_number = random.randint(low,high)
        print(f"PC's number is {pc_number}")
        result = str(input("If its too low (L), too high (H), correct (C):"))
        if result == "L":
            low = pc_number + 1
        elif result == "H":
            high = pc_number - 1

    print("Your PC si smart zulul :D it has just guessed the number!")

computer_guessing(100)
time.sleep(2)
        
