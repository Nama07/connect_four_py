rows, cols = (6, 7)
play = True

board = [["o" for _ in range(cols)] for _ in range(rows)]


def print_board():
    for row in board:
        print(" ".join(row))
    print()


def drop_token(column, player_symbol):
    for row in range(rows - 1, -1, -1): 
        if board[row][column] == "o":
            board[row][column] = player_symbol
            return row, column 
    return None, None


def check_win(row, col, player_symbol):
    directions = [
        (0, 1),   
        (1, 0),  
        (1, 1),  
        (1, -1)  
    ]

    for dr, dc in directions:
        count = 1  


        for direction in [1, -1]:
            r, c = row, col
            while True:
                r += dr * direction
                c += dc * direction
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == player_symbol:
                    count += 1
                else:
                    break

        if count >= 4:
            return True

    return False


current_player = "x"

while play:
    print_board()

    try:
        column_choice = int(input(f"Player {current_player}, choose a column (0-{cols - 1}): "))
        if column_choice < 0 or column_choice >= cols:
            print("Invalid column. Try again.")
            continue

        row, col = drop_token(column_choice, current_player)
        if row is None:
            print("Column is full! Try a different one.")
            continue

        if check_win(row, col, current_player):
            print_board()
            print(f" Player {current_player} wins! ")
            break


        current_player = "@" if current_player == "x" else "x"

    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nGame interrupted.")
        play = False
