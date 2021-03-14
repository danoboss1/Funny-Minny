import random, string, time
from words import words


word = random.choice(words).upper()
guessing_word = ""
letters = set(string.ascii_uppercase)
used_letters = []
word_letters = set(word)
word_list = ["_"]
lives = 6

while "_" in word_list:
    print("Number of lifes:", lives)
    print("Used letters are: ", ' '.join(used_letters))
    x = input("Guess the letter: ").upper()
    used_letters.append(x)

    
    #toto by malo napisat dane slovo
    word_list = [letter if letter in used_letters else "_" for letter in word]
    print("Current word: ", ' '.join(word_list), "\n")

    if x not in word_list:
        lives = lives - 1

    if lives == 0:
        word_list = ["you lost"]
        
    
if lives == 0:
    print("You lost! The word was:", word)
else:
    print("You won!") 

time.sleep(5)

    

    

