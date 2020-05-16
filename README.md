# Refatoração

Minhas anotações e códigos do curso [Refatoração na prática](https://henriquebastos.net/produtos/refatoracao-na-pratica/).

## Primeiro módulo

Anotações: [Conceitos iniciais](aulas/01_conceitos_iniciais.md) &emsp;&emsp; [Essência da refatoração](aulas/02_essencia_refatoracao.md)

Código: [donuts](code/donuts.py) &emsp; [testes](code/tests/test_donuts.py)

A evolução do código e dos testes pode ser verificada no histórico de commits.

## Segundo módulo

Anotações: [Dimensões dos componentes](aulas/03_dimensoes_componentes.md)

Código: [wordcount](code/wordcount.py) &emsp; [testes](code/tests/test_wordcount.py)

A evolução do código e dos testes pode ser verificada no histórico de commits.

## Módulo final

Anotações: [Refatoração rápida](aulas/04_refatoracao_rapida.md)

No módulo final foi feita a análise de um código [desse projeto](https://github.com/henriquebastos/changeMatrix/tree/460de003d4663a4480274cda159ce871bb20a89e). O link anterior é do código original, sem testes e com várias possibilidades de melhora. Foi feita uma análise do que se poderia melhorar, marcando com a tag TODO no código conforme [esse link](https://github.com/henriquebastos/changeMatrix/tree/f9d8da91866b3c3942f3e5bc213b662a4c0a50e5). Por fim, foi feita uma refatoração passo a passo do código, após elaborar testes. A versão final está nesse repositório no arquivo `matriz.py`. Uma versão simplificada de um [game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) foi feita aproveitando a lógica extraída do código de matriz, conforme disponível no arquivo `gameoflife.py`. A evolução dos códigos e dos testes pode ser verificada no histórico de commits.