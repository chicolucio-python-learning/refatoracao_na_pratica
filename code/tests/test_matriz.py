from matriz import create_array, string
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
