#inspirated by Kylie Ying, check out her Youtube
import time

print("Welcome to the Harry Potter's Madlib")
time.sleep(1)

info = input("Write 1 if u know what is Madlib and 0 if not:")

if info == "1":
    pass
else:
    print("""\n The game consists of multiple rounds. During each round,
          a Sentence card is revealed and read aloud. Next,
          all players will choose Word cards from their hands to fill
          in all the blanks in the sentence. When all players are ready,
          each player will read the sentence with their chosen words filled in,
          then everyone votes.""")

time.sleep(1)
print("Lets begin")
interjection1 = input("interjection:")
noun1 = input("noun:")
verb1 = input("verb:")
noun2 = input("noun:")
adjective1 = input("adjective:")
noun3 = input("noun:")

madlib = f"""{interjection1}! she screeched. Harry heard her walking toward the
{noun1} and then the sound of the frying pan being put on the stove.
He rolled onto his back and tried to {verb1} the {noun2} he had been having.
It had been a good one. There had been a {adjective1}
motorcycle in it.
He had a funny feeling he'd had the same {noun3} before."""

print(madlib)


input()
