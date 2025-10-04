import json
import random

def loadQuestions():
    try:
        with open('questions.json') as jf:
            q = json.load(jf)
    except FileNotFoundError:
        print("ERROR: File not found.")
    return q

def printQuestion(question):
    print(question['question'])
    print(question['options'])

def game():
    points = 0
    incorrect = []
    questions = loadQuestions()
    print("\n--- Programming Quiz ---")
    while True:
        try:
            total = int(input("Input number of questions you want: "))
            if total > len(questions):
                print("Not enaugh questions.")
            else:
                break
        except ValueError:
            print("ERROR: Invalid value.")
    n = 1
    question = random.sample(questions, total)
    while n <= total:
        print("\n--- Programming Quiz ---")
        print(f"Question nr.: {n}")
        printQuestion(question[n - 1])
        a = input("Input your answer: ")
        a = a.upper()
        if a == question[n - 1]['answer']:
            points += 1
        else:
            incorrect.append([question[n - 1]['question'], question[n - 1]['answer']])
        n += 1
    print(f"Your result is: {points}/{total}")
    if incorrect:
        for q in incorrect:
            print(f"You were wrong in '{q[0]}' and correct answer was ({q[1]}).")
    else:
        print("Congratulations! You answered correct for all questions!")
        



game()