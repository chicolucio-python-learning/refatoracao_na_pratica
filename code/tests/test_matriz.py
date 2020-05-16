from matriz import (string,  parse, invoke)
from unittest.mock import patch
import io

from textwrap import dedent
import pytest


@pytest.fixture
def board():
    board = []
    invoke(board, ['I', 4, 5])
    return board


def test_create(board):
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


def test_clean():
    board = []
    invoke(board, ['I', 4, 5, 'X'])
    invoke(board, ['C'])
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


def test_pixel(board):
    invoke(board, ['L', 2, 2, 'W'])
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OOOO
        OOOO
        OOOO'''
    )


def test_vertical(board):
    invoke(board, ['V', 2, 2, 4, 'W'])
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OWOO
        OWOO
        OOOO'''
    )


def test_horizontal(board):
    invoke(board, ['H', 2, 3, 3, 'W'])
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OWWO
        OOOO
        OOOO'''
    )


def test_block(board):
    invoke(board, ['K', 2, 2, 3, 4, 'W'])
    assert string(board) == dedent(
        '''\
        OOOO
        OWWO
        OWWO
        OWWO
        OOOO'''
    )


def test_fill(board):
    for n in range(1, 5):
        invoke(board, ['L', n, n, 'X'])
    invoke(board, ['F', 3, 2, '+'])
    assert string(board) == dedent(
        '''\
        X+++
        OX++
        OOX+
        OOOX
        OOOO'''
    )


def test_save(board):
    with patch('builtins.open', spec=io.IOBase) as mock:
        invoke(board, ['S', 'out.bmp'])

    file = mock.return_value.__enter__.return_value
    file.write.assert_called_once_with(string(board))


def test_parser():
    assert parse('X') == ['X']
    assert parse('I 4 5') == ['I', 4, 5]
    assert parse('F 3 2 +') == ['F', 3, 2, '+']
    assert parse('K 2 2 3 4 W') == ['K', 2, 2, 3, 4, 'W']
    assert parse('S out.bmp') == ['S', 'OUT.BMP']

    assert parse('   X   ') == ['X']

    with pytest.raises(ValueError):
        parse('')
        parse('!')
