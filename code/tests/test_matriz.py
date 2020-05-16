from matriz import (create_array, string, clean_array, color_pixel, ver_pixel, hor_pixel,
                    block_pixel, save_array, fill_pixel)
from unittest.mock import patch
import io

from textwrap import dedent
import pytest


@pytest.fixture
def board():
    return create_array(4, 5)


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
    board = create_array(4, 5, 'X')
    board = clean_array(board)
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )


def test_pixel(board):
    board = color_pixel(board, (2, 2), 'W')
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OOOO
        OOOO
        OOOO'''
    )


def test_vertical(board):
    board = ver_pixel(board, 2, 2, 4, 'W')
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OWOO
        OWOO
        OOOO'''
    )


def test_horizontal(board):
    board = hor_pixel(board, 2, 3, 3, 'W')
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OWWO
        OOOO
        OOOO'''
    )


def test_block(board):
    board = block_pixel(board, 2, 2, 3, 4, 'W')
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
        color_pixel(board, (n, n), 'X')
    board = fill_pixel(board, (3, 2), '+')
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
        save_array('out.bmp', board)

    file = mock.return_value.__enter__.return_value
    file.write.assert_called_once_with(string(board))
