import string
from collections import Counter

def clean_text(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower().split()

def loadFile(fileName):
    try:
        with open(fileName, 'r') as f:
            return clean_text(f.read())
    except FileNotFoundError:
        print("ERROR: File not found.")
        return []

def wordCount(text):
    if not text:
        print("No words to count.")
        return
    
    total_words = len(text)
    unique_words = set(text)
    avg_wrods = sum(len(w) for w in text) // total_words
    counter = Counter(text)
    most_common_word, count = counter.most_common(1)[0]

    print(f"You have {total_words} word/s.")
    print(f"Number of unique words: {len(unique_words)}")
    print(f"Average word length is {avg_wrods}")
    print(f"Most common word: '{most_common_word}' ({count} times)")

def menu():
    while True:
        print("--- Word Counter ---")
        print("1. Count words from file.")
        print("2. Count words from text.")
        print("3. End")
        while True:
            try:
                m = int(input("Choose your action: "))
                break
            except ValueError:
                print("ERROR: Invalid action.")
        if m == 1:
            fileName = input("Input your file name: ")
            text = loadFile(fileName)
        elif m == 2:
            text = input("Input your text: ")
            text = clean_text(text)
        elif m == 3:
            print("Bye")
            break
        else:
            print("Invalid action.")
        print('\n')
        wordCount(text)
        print('\n')

menu()