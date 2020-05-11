# -*- coding: utf8 -*-


def read_sequence():  # Read and validate a sequence of commands.
    charValid = ("ICLVHKFSX")
    sqc = input("Digite um comando: ").upper()
    sqc = sqc.split()

    for char in charValid:
        if char == sqc[0] and not "":
            return sqc
    else:
        print("\nComando Inválido!\n")
        return sqc


def print_board(board):  # Print the Board.
    print("\n")
    for row in board:
        print("".join(row))
    print("\n")


def create_array(cmd):  # Create a array - 'I' Command.
    board = []
    col, line = cmd

    for x in range(int(line)):
        board.append(["O"] * int(col))
    return board


def clean_array(board):  # Clean a array - 'C' Command.
    for line in range(0, len(board)):
        for col in range(0, len(board[line])):
            board[line][col] = "O"
    return board


def color_pixel(cmd, board):  # Change the color of one pixel - 'L' Command.
    col, line, color = cmd

    board[int(line) - 1][int(col) - 1] = color
    return board


def ver_pixel(cmd, board):  # Change the color of a column - 'V' Command.
    col, lineIni, lineEnd, C = cmd

    for ver in range(int(lineIni) - 1, int(lineEnd)):
        board[int(ver)][int(col) - 1] = C
    return board


def hor_pixel(cmd, board):  # Change the color of a line - 'H' Command.
    colIni, colEnd, line, color = cmd

    for hor in range(int(colIni) - 1, int(colEnd)):
        board[int(line) - 1][int(hor)] = color
    return board


def block_pixel(cmd, board):  # Change color of an entire block - 'K' Command.
    colIni, lineIni, colEnd, lineEnd, color = cmd

    for hor in range(int(colIni) - 1, int(colEnd)):
        for ver in range(int(lineIni) - 1, int(lineEnd)):
            board[int(ver)][int(hor)] = color
    return board


def out_range(board, Y, X):  # Check if a cmd is out of list range.
    line = len(board)
    col = len(board[0])

    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):  # Fill a continuous region 'F' command.
    col, line, chgColor = cmd

    color = board[line][col]

    if out_range(board, line, col):
        board[line][col] = chgColor

        if out_range(board, line, col - 1):
            if board[line][col - 1] == color:
                fill_pixel([col - 1, line, chgColor], board)

        if out_range(board, line, col + 1):
            if board[line][col + 1] == color:
                fill_pixel([col + 1, line, chgColor], board)

        if out_range(board, line - 1, col):
            if board[line - 1][col] == color:
                fill_pixel([col, line - 1, chgColor], board)

        if out_range(board, line + 1, col):
            if board[line + 1][col] == color:
                fill_pixel([col, line + 1, chgColor], board)

    return board


def save_array(name, board):  # Save the array with the 'S' command.
    with open(name.lower(), "w") as my_file:
        for item in board:
            my_file.write("".join(item) + "\n")


def main():
    while True:
        try:
            cmd = read_sequence()

            if cmd[0] == "X":
                break

            elif cmd[0] == "I":
                board = create_array(cmd[1:3])

            elif cmd[0] == "L":
                board = color_pixel(cmd[1:4], board)

            elif cmd[0] == "V":
                board = ver_pixel(cmd[1:5], board)

            elif cmd[0] == "H":
                board = hor_pixel(cmd[1:5], board)

            elif cmd[0] == "K":
                board = block_pixel(cmd[1:6], board)

            elif cmd[0] == "F":
                cmd[1] = int(cmd[1]) - 1
                cmd[2] = int(cmd[2]) - 1
                board = fill_pixel(cmd[1:4], board)

            elif cmd[0] == "S":
                save_array(cmd[1], board)

            elif cmd[0] == "C":
                board = clean_array(board)

            else:
                continue

            print_board(board)

        except:
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
