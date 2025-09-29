from random import choice

HANGMANPICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def loadWords():
    try:
        with open('words.txt', 'r') as w:
            words = [w.lower() for w in w.read().split()]
    except FileNotFoundError:
        print("ERROR: File not found.")
        exit()
    return words

def hiddenWord(word):
    hw = []
    for i in word:
        hw.append('_')
    return hw

def printLifes(n):
    stage = 6 - n
    print(HANGMANPICS[stage])
    
def printGuesses(guesses):
    print("Guesses: ",", ".join(guesses))    

def printHidden(hidden):
    hw = ''
    for i in hidden:
        hw += i + ' '
    print(f"{hw}\n")

def game():
    words = loadWords()
    w = choice(words)
    word = []
    guesses = []
    lifes = 6
    word = list(w)
    l = len(word)

    hw = hiddenWord(word)
    while True:
        print("--- HANGMAN GAME ---\n")
        print("Hidden word:")
        printHidden(hw)
        guess = input("Guess letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Incorrect number of letters")
        else:
            if guess in guesses:
                print(f"'{guess}' was already guessed.")
            elif guess in word:
                idx = [i for i, x in enumerate(word) if x == guess]
                for i in idx:
                    hw[i] = guess
                    l -= 1
                guesses.append(guess)
                print('Your guess is correct!')
            else:
                lifes -= 1
                guesses.append(guess)
                print("This letter is not part of this word.")
        print("Lifes left:")
        printLifes(lifes)
        printGuesses(guesses)
        if lifes == 0:
            print("💀 GAME OVER – You lost!")
            print(f"The hidden word was: {"".join(word)}")
            break
        elif l == 0:
            print("🎉 Congratulations – You won!")
            print(f"The hidden word was: {"".join(word)}")
            break
game()
