import random

def roll():
    global truenum
    num = [i for i in str(random.randint(1000,9999))]
    truenum = [i for i in num if num.count(i) == 1 ]

    if len(truenum) < 4:
        roll()

        
roll()


def play():
    for g in range(15):
        guess = [i for i in input('take a guess: ')]
        
        bull = 0
        hit = 0
        
        for i in guess:

            if i in truenum:

                if guess.index(i) == truenum.index(i):
                    bull += 1
                else:
                    hit+= 1
                    
        print(f'{truenum}')
        print(f'בול: {bull} פגיעה: {hit}')
        print('tries left: ' + str(14 - int(g)))
        
        if guess == truenum:
            print(f"you guessed the number! it was {''.join(truenum)}")
            break
    if guess != truenum:
        print(f"you lost .. number was: {''.join(truenum)}")


play()
