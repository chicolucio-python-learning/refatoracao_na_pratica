from wordcount import main
import sys

# setup
FILE = "code/letras.txt"
FILE_EXP_PRINT_WORDS = "code/tests/expected_print_words.txt"
FILE_EXP_PRINT_TOP = "code/tests/expected_print_top.txt"

with open(FILE_EXP_PRINT_WORDS) as file:
    out_print_words = file.read()

with open(FILE_EXP_PRINT_TOP) as file:
    out_print_top = file.read()

d = {'a': 2, 'b': 4, 'c': 3}


def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['wordcount.py', mode, FILE])
    main()
    out, _ = capsys.readouterr()
    return out


def test_count(capsys, monkeypatch):
    assert run('--count', capsys, monkeypatch) == out_print_words


def test_topcount(capsys, monkeypatch):
    assert run('--topcount', capsys, monkeypatch) == out_print_top
