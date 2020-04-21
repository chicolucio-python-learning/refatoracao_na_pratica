"""
13. wordcount
Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.
A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.
Por exemplo:
$ python wordcount.py --count letras.txt
a 2
b 4
c 3
B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem decrescente de ocorrências.
Por exemplo:
$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2
Abaixo já existe um esqueleto do programa para você preencher.
Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.
Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys


# SEU CÓDIGO AQUI...

FILE = "./letras.txt"


def wordcount_dict(filename):
    with open(filename) as file:
        file_content = file.read()
    words = file_content.lower().split()
    words_dict = {}

    for w in words:
        if w not in words_dict:
            words_dict[w] = 0
        words_dict[w] += 1
    return words_dict.items()


def print_words(filename):
    word_count = wordcount_dict(filename)
    word_count = sorted(word_count)
    l = []
    for key, value in word_count:
        l.append(f'{key} {value}')
    out = '\n'.join(l)
    return out


def print_top(filename):
    word_count = wordcount_dict(filename)
    word_count = sorted(word_count,
                        key=lambda item: item[-1], reverse=True)[:20]
    l = []
    for key, value in word_count:
        l.append(f'{key} {value}')
    out = '\n'.join(l)
    return out

# A função abaixo chama print_words() ou print_top() de acordo com os
# parâmetros do programa.


def main():
    if len(sys.argv) != 3:
        print('Utilização: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print(print_words(filename))
    elif option == '--topcount':
        print(print_top(filename))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
