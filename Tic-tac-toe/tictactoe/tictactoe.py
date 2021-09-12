letters = ["X", "O"]


def create_matrix(some_string):
    matrix = []
    n = 0
    start = 6
    end = 9
    while n < 3:
        row = list(some_string[start:end])
        start -= 3
        end -= 3
        n += 1
        matrix.append(row)
    return matrix

def check_game(some_string, matrix):
    check_win = check_winner(matrix)
    if some_string.count("X") - some_string.count("O") >= 2 or some_string.count("O") - some_string.count("X") >= 2:
        return "Impossible"
    elif len(check_win) > 1:
        return "Impossible"
    elif len(check_win) == 1:
        return f"{check_win[0]} wins"
    elif " " in some_string or "_" in some_string:
        return "Game not finished"
    else:
        return "Draw"


# def check_winner(some_string, letters):
#     row = some_string
#     check_impossible = []
#     all_wins = [row[:3], row[3:6], row[6:], row[0] + row[3] + row[6], row[1] + row[4] + row[7],
#                 row[2] + row[5] + row[8],
#                 row[0] + row[4] + row[8], row[2] + row[4] + row[6]]
#     for one_row in all_wins:
#         for letter in letters:
#             if str(one_row).count(letter) == 3:
#                 check_impossible.append(letter)
#     return check_impossible

def check_winner(matrix):
    check_impossible = []
    all_wins_combo = [matrix[2][2] + matrix[2][1] + matrix[2][0], matrix[1][2] + matrix[1][1] + matrix[1][0],
                      matrix[0][2] + matrix[0][1] + matrix[0][0], matrix[2][0] + matrix[1][0] + matrix[0][0],
                      matrix[2][1] + matrix[1][1] + matrix[0][1], matrix[2][2] + matrix[1][2] + matrix[0][2],
                      matrix[2][0] + matrix[1][1] + matrix[0][2], matrix[2][2] + matrix[1][1] + matrix[0][0]]
    for one_row in all_wins_combo:
         for letter in letters:
             if str(one_row).count(letter) == 3:
                check_impossible.append(letter)
    return check_impossible


def convert_string_to_coord(user_input):
    return user_input.split()

def enter_validate_coordinates():
    checked_list = []
    while len(checked_list) < 2:
        user_input = convert_string_to_coord(input("Enter the coordinates:"))
        for sym in user_input:
            if sym.isalpha():
                print("You should enter numbers!")
                checked_list = []
                break
            if int(sym) > 3 or int(sym) < 1:
                print("Coordinates should be from 1 to 3!")
                checked_list = []
                break
            else:
                checked_list.append(int(sym))
    return checked_list


def check_coordinates(coordinates, use_matrix):
    for letter in letters:
        if letter in use_matrix[coordinates[1] - 1][coordinates[0] - 1]:
            return True
        else:
            continue
    return False

def add_move(use_matrix, right_coord, mover):
    new_matrix = use_matrix
    new_matrix[right_coord[1] - 1][right_coord[0] - 1] = mover
    return new_matrix

def show(str_field):
    print("---------")
    print(f"| {str_field[0]} {str_field[1]} {str_field[2]} |")
    print(f"| {str_field[3]} {str_field[4]} {str_field[5]} |")
    print(f"| {str_field[6]} {str_field[7]} {str_field[8]} |")
    print("---------")

def matrix_show(matrix):
    print("---------")
    print(f"| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |")
    print(f"| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |")
    print(f"| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |")
    print("---------")

def create_move(mover, matrix):
    while True:
        coordinates = enter_validate_coordinates()
        if check_coordinates(coordinates, matrix):
            print("This cell is occupied! Choose another one!")
            continue
        else:
            new_matrix_field = add_move(matrix, coordinates, mover)
            matrix_show(new_matrix_field)
            return new_matrix_field


def start_game(matrix):
    game_field = matrix
    # row = "".join(matrix[2]) + "".join(matrix[1]) + "".join(matrix[0])
    mover = "O"
    while True:
        if mover == "O":
            mover = "X"
        else:
            mover = "O"
        matrix_show(game_field)
        game_field = create_move(mover, game_field)
        check = check_game("".join(game_field[2]) + "".join(game_field[1]) + "".join(game_field[0]), game_field)
        if check == "Game not finished":
            continue
        if check == "X wins" or check == "O wins":
            print(check)
            break
        if check == "Draw":
            print(check)
            break



# line = input("Enter cells:")
# matrix_field = create_matrix(line)
# matrix_show(matrix_field)
# while True:
#     coordinates = enter_validate_coordinates()
#     if check_coordinates(coordinates, matrix_field):
#         print("This cell is occupied! Choose another one!")
#         continue
#     else:
#         new_matrix_field = add_move(matrix_field, coordinates)
#         matrix_show(new_matrix_field)
#         break


#print(check_game(line))


empty_matrix = create_matrix("         ")
start_game(empty_matrix)
#check_winner(empty_matrix)