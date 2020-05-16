from matriz import create_array, set_many, string, coords_of, get_item, offset, set_item, items, get_many
from os import system
from copy import deepcopy
from time import sleep

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

WIDTH, HEIGHT = 50, 25

GLIDER = ((2, 1), (3, 2), (1, 3), (2, 3), (3, 3))
SURROUNDING = tuple((a, b) for a in range(-1, 2) for b in range(-1, 2) if not (a == b == 0))


def neighbors(c):
    yield from (offset(c, r) for r in SURROUNDING)


def wrap(c):
    yield from ((a % WIDTH, b % HEIGHT) for a, b in c)


def should_die(total):
    return total < 2 or total > 3


def should_ressurect(total):
    return total == 3


def rule(coord, status, total):

    s = status
    if status == LIVE:
        if should_die(total):
            s = DEAD
    else:
        if should_ressurect(total):
            s = LIVE
    return s


def how_many_alive(ns):
    return sum(1 for s in ns if s == LIVE)


def main():
    board = []
    create_array(board, WIDTH, HEIGHT, DEAD)
    set_many(board, GLIDER, LIVE)

    while True:
        system('clear')
        print(string(board))

        new_board = deepcopy(board)

        for coord, status in items(board):
            ncoords = wrap(neighbors(coord))
            nstatus = get_many(board, ncoords)
            total = how_many_alive(nstatus)

            set_item(new_board, coord, rule(coord, status, total))

        board = new_board
        sleep(0.05)


if __name__ == "__main__":
    main()
