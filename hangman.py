
import random

with open(r'C:\Users\User\Desktop\תכנות\python\wordlist.txt', 'r') as wordfile:
    wordlist = [line[:-1] for line in wordfile]  # creates a list of all the words in the file

word = random.choice(wordlist)  # choose random word from the list

letterlist = [letter for letter in word]  # the word converted into a list of letters

secretlist = ['_' for letter in word]  # the secret word as ( _ _ _ )

print('start playing\n')
print(' '.join(secretlist) + '\n')


def start_playing():
    guess = input('guess a letter: ')

    while len(guess) > 1 or (not (guess >= 'a' and guess <= 'z')) and (not (guess >= 'A' and guess <= 'Z')):
        guess = input('that aint a letter,guess a letter: ')  # char validation

    [secretlist.pop(i) and secretlist.insert(i, char) for i, char in enumerate(word) if guess == char]  # if guess is correct show the letter

    print('\n' + ' '.join(secretlist))


for i in range(15):
    start_playing()
    print('tries left: ' + str(14 - i))
    if letterlist == secretlist:
        print('you won!')
        break
if not letterlist == secretlist:
    print(f'you lost!  the word was: {word}')
