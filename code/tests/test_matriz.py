from matriz import create_array, string
from textwrap import dedent


def test_string():
    board = create_array(['4', '5'])
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


def test_create():
    board = create_array(['4', '5'])

    assert len(board) == 5 and len(board[0]) == 4
