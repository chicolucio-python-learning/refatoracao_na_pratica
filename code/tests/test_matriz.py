from matriz import create_array


def test_create():
    board = create_array(['4', '5'])

    assert len(board) == 5 and len(board[0]) == 4
