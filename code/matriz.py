# -*- coding: utf8 -*-

BLANK = "O"


def width(board):
    return len(board[0])


def height(board):
    return len(board)


def x(coord):
    return coord[0]


def y(coord):
    return coord[1]


def set_item(board, coord, value):
    board[y(coord)-1][x(coord)-1] = value


def set_many(board, coords, value):
    for c in coords:
        set_item(board, c, value)


def coords_of(board):
    yield from region(1, 1, width(board), height(board))


def region(col_start, row_start, col_end, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield col, row


def create_array(cmd, value=BLANK):
    """Create a array - 'I' Command."""
    col, row = int(cmd[0]), int(cmd[1])  # TODO
    return [[value] * col for _ in range(row)]


def clean_array(board, value=BLANK):
    """Clean a array - 'C' Command."""
    set_many(board, coords_of(board), value)
    return board


def color_pixel(cmd, board):
    """Change the color of one pixel - 'L' Command."""
    coord, color = (int(cmd[0]), int(cmd[1])), cmd[2]
    set_item(board, coord, color)
    return board


def ver_pixel(cmd, board):
    """Change the color of a column - 'V' Command."""
    col, row_start, row_end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]

    set_many(board, region(col, row_start, col, row_end), color)

    return board


def hor_pixel(cmd, board):
    """Change the color of a line - 'H' Command."""
    col_start, col_end, row, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), cmd[3]

    set_many(board, region(col_start, row, col_end, row), color)
    return board


def block_pixel(cmd, board):
    """Change color of an entire block - 'K' Command."""
    col_start, row_start, col_end, row_end, color = int(cmd[0]), int(cmd[1]), int(cmd[2]), int(cmd[3]), cmd[4]

    set_many(board, region(col_start, row_start, col_end, row_end), color)
    return board


def out_range(board, Y, X):
    """Check if a cmd is out of list range."""
    # TODO: Ajustar a ordem de argumentos para respeitar a lógica de um par ordenado.
    # TODO: Melhorar o nome out_range, pois ele está muito atrelado ao detalhe de implementação com listas.
    # TODO: Verificar se essa função não poderia ser substituida pelo método __contains__ -> Coord(x, y) in board
    # TODO: Renomar para width e height.
    line = len(board)
    col = len(board[0])

    # TODO: Retonar o resultado da expressão lógica.
    # TODO: Utilizar comparações ricas. 0 <= X < width
    # TODO: Alinhar a lógica do retorno com o nome da função.
    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):
    """Fill a continuous region 'F' command."""
    # TODO: Melhorar o nome fill_pixel.
    # TODO: Expandir cmd para os parâmetros já com os tipos corretos.

    col, line, chgColor = cmd

    # TODO: Melhorar o nome da variável color para enfatizar que se trata de uma cor original/anterior.
    # TODO: fill_pixel não deveria conhecer os detalhes de implementação do board.
    color = board[line][col]

    # TODO: Inverter a lógica para parar caso esteja fora.
    if out_range(board, line, col):
        # TODO: Melhorar o nome chgColor para algo mais descritivo.
        board[line][col] = chgColor

        # TODO: Trazer o teste da cor para junto do out_range com um and.
        # TODO: Extrair a coordenada para variáveis auxiliares.
        # TODO: Computar as coordenadas dos vizinhos antes e chamá-las em um loop.
        # TODO: Encapsular o teste do vizinho em uma pequena função auxiliar. (?)
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


def save_array(name, board):
    """Save the array with the 'S' command."""
    # TODO: Melhorar o nome save_array.
    # TODO: Melhorar o nome do parâmetro name.
    # TODO: Utilizar a mesma lógica do "board as string" para persistir no arquivo texto.

    # TODO: remover o lower.
    # TODO: melhorar o my_file para f.
    with open(name.lower(), "w") as my_file:
        for item in board:
            my_file.write("".join(item) + "\n")


def read_sequence():
    """Read and validate a sequence of commands."""
    # TODO: Melhorar o nome read_sequence, pois na verdade ela lê o comando.
    # TODO: Separar as responsabilidades do read_sequence para garantir a leitura de um comando válido e
    #       validar o comando em si.
    # TODO: Verificar se faz sentido ter um parser único para o comando validado, eliminando List[str] e usando algo
    #       de mais alto nível.

    # TODO: Melhorar o nome charValid para algo mais semântico.
    # TODO: Remover os parêntesis desnecessários.
    charValid = ("ICLVHKFSX")
    # TODO: Melhorar o nome sqc. Sugestão: cmd
    # TODO: Separar a obtenção do comando, do tratamento do comando.
    sqc = input("Digite um comando: ").upper()
    sqc = sqc.split()

    for char in charValid:
        # TODO: Verificar a real necessidade desse "and".
        if char == sqc[0] and not "":
            return sqc
    else:
        print("\nComando Inválido!\n")
        return sqc
    # TODO: Implementar um único return.


def string(board):
    return '\n'.join((''.join(row) for row in board))


def print_board(board):
    """Print the Board."""
    print("\n")
    print(string(board))
    print("\n")


def main():
    # TODO: Substituir o uso do if/elif por um mapeament com dicionário.
    # TODO: Encapsular os detalhes do comando sem vazar para o main.
    # TODO: Extrair a definição do board para o início do processamento.
    # TODO: Verificar a possibilidade do board ser uma instância de uma classe.
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
                # TODO: Encapsular a conversão de índices do board.
                cmd[1] = int(cmd[1]) - 1
                cmd[2] = int(cmd[2]) - 1
                board = fill_pixel(cmd[1:4], board)

            elif cmd[0] == "S":
                save_array(cmd[1], board)

            elif cmd[0] == "C":
                board = clean_array(board)

            else:
                # TODO: Remover quando a validação do comando for encapsulada no read_sequence.
                continue

            # TODO: Extrair o print do print_board.
            print_board(board)

        except:
            # TODO: Especificar as exception que serão tratadas.
            # TODO: Verificar como isolar a validação do comando no read_sequence.
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
