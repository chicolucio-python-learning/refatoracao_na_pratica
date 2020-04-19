from wordcount import dict_wordcount, print_words, print_top


FILE = "code/letras.txt"
FILE_EXP_PRINT_WORDS = "code/tests/expected_print_words.txt"
FILE_EXP_PRINT_TOP = "code/tests/expected_print_top.txt"

with open(FILE_EXP_PRINT_WORDS) as file:
    out_print_words = file.read()

with open(FILE_EXP_PRINT_TOP) as file:
    out_print_top = file.read()

d = {'a': 2, 'b': 4, 'c': 3}


def test_dict_wordcount():
    assert dict_wordcount(FILE) == d


def test_print_words(capsys):
    print_words(FILE)
    out, _ = capsys.readouterr()
    assert out == out_print_words


def test_print_top(capsys):
    print_top(FILE)
    out, _ = capsys.readouterr()
    assert out == out_print_top
