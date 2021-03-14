import random, time

def play():
    you = input("Pick between rock, paper and scissors:")
    pc = random.choice(["rock","paper","scissors"])

    while pc == you:
        print("u have choosen the same")
        you = input("Pick between rock, paper and scissors:")
        pc = random.choice(["rock","paper","scissors"])

    #p>r r>s s>p

    if (pc == "rock" and you == "scissors") or (pc == "paper" and you == "rock") or \
        (pc == "scissors" and you == "paper"):

        print(f"(you) {you} vs (pc) {pc}")
        print("YOU LOST!")

    else:
        print(f"(you) {you} vs (pc) {pc}")
        print("YOU WON!")

play()

time.sleep(5)
              
    
