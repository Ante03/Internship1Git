
def check_winner(game):
    if game[0] == game[1] == game[2] and game [0] != " ":
        return True
    elif game[0] == game[4] == game[8] and game [0] != " ":
        return True
    elif game[0] == game[3] == game[6] and game [0] != " ":
        return True
    elif game[3] == game[4] == game[5] and game [3] != " ":
        return True
    elif game[6] == game[7] == game[8] and game [6] != " ":
        return True
    elif game[6] == game[4] == game[2] and game [6] != " ":
        return True
    elif game[2] == game[5] == game[8] and game [2] != " ":
        return True
    elif game[1] == game[4] == game[7] and game [1] != " ":
        return True
    else:
        return False

def check_letter(player):
    if player == "X" or player == "O":
        return True
    else:
        return False

def print_game(game):
    print(f"{game[0]} | {game[1]} | {game[2]}")
    print("--+---+--")
    print(f"{game[3]} | {game[4]} | {game[5]}")
    print("--+---+--")
    print(f"{game[6]} | {game[7]} | {game[8]}")

def main():
    game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    while True:
        field = int(input("Enter field(1-9): "))
        field -= 1
        if field < 9 or field > -1:
            if game[field] == " ":
                player = input("(X or O): ")
                if check_letter(player):
                    game[field] = player
                    print_game(game)
                    if check_winner(game):
                        print(f"{player} won!")
                        break
                else:
                    print("Unesite odgovarajucu vrijednost!")
            else:
                print("Unesite slobodno polje!")
        else:
            print("Unesite polje izmedu 1 i 9!")



if __name__ == '__main__':
    main()