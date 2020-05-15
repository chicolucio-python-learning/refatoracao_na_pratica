from matriz import create_array, string, clean_array
from textwrap import dedent


def test_create():
    board = create_array(['4', '5'])
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


def test_clean():
    board = create_array(['4', '5'], 'X')
    board = clean_array(board)
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )
