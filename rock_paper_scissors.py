from random import choice

def botChoice(opt):
    return choice(opt)

def checkWinner(player_move, ai_move):
    winComb = [["paper", "rock"], ["scissors", "paper"], ["rock", "scissors"]]
    if player_move == ai_move:
        print("DRAW")
        return 0
    for i in winComb:
        if player_move == i[0] and ai_move == i[1]:
            print("You Win this round!")
            return 1
    print("You Lose this round")
    return -1

def printOptions(opt):
    for i, o in enumerate(opt):
        print(f"{i + 1}. {o}")

def game():
    print("--- Rock Paper Scissors ---")
    opt = ["rock", "paper", "scissors"]
    while True:
        try:
            total = int(input("Choose round numbers: "))
            if total > 0:
                break
            else:
                print("Number of rounds must be higher than 0.")
        except ValueError:
            print("ERROR: Invalid value")
    n, p_points, ai_points = 1, 0, 0
    while n <= total:
        print(f"Round number {n}")
        printOptions(opt)
        while True:
            try:
                o = int(input("Choose your action: "))
                if 1 <= o <= 3:
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("ERROR: Invalid value.")
        player_move = opt[o - 1]
        ai_move = botChoice(opt)
        print(f"AI move: {ai_move}")

        p = checkWinner(player_move, ai_move)
        if p == 1:
            p_points += 1
        elif p == -1:
            ai_points += 1
        n += 1
    print("Game results: ")
    if p_points > ai_points:
        print("Congratulations you won!")
    elif p_points < ai_points:
        print("You lost.")
    else:
        print("Draw.")
    print(f"You: {p_points}, AI: {ai_points}")

game()