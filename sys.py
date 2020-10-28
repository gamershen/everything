import sys
import random


first = sys.argv[1]
second = sys.argv[2]

rnd = random.randint(int(first),int(second))
tries = round((int(second) - int(first)) /2 ) + 1

def make_sure():
    print("guess out of range, please try again")
        
    
print(f"Game Started! you have {tries} tries\n")


for i in range(1,tries+1):
    
    answer = input("guess a number: ")

    if int(answer) < int(first) or int(answer) > int(second):
        make_sure()

    elif int(answer) == rnd:
        print(f"you right, the number was {rnd}")
        break
    
    else:
        print("wrong, tries left: " + str(tries -i) + "\n")
    
if int(answer) != rnd:
    print(f"you lost, the number was {rnd}")

