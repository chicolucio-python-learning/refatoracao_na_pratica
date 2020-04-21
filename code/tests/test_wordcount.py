from wordcount import wordcount_dict, print_words, print_top, main
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


# testes funções


def test_dict_wordcount():
    assert wordcount_dict(FILE) == d.items()


def test_print_words(capsys):
    assert print_words(FILE) == 'a 2\nb 4\nc 3'


def test_print_top(capsys):
    assert print_top(FILE) == 'b 4\nc 3\na 2'


# testes CLI


def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['wordcount.py', mode, FILE])
    main()
    out, _ = capsys.readouterr()
    return out


def test_count(capsys, monkeypatch):
    assert run('--count', capsys, monkeypatch) == out_print_words


def test_topcount(capsys, monkeypatch):
    assert run('--topcount', capsys, monkeypatch) == out_print_top
