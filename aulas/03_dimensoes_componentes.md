# As dimensões dos componentes

Já vimos:
- Refatoração tem uma motivação econômica

Da nossa prática:
- se perde controle de um código rapidamente

## A crise do software

- década de 60
- Douglas Mcllroy
  - participou do Unix
  - conceito de pipeline:
    - programas com propósitos específicos conectados
      - saída de um é a entrada de outro
  - reutilização de programas
    - componentes
    - a discussão deve ser quais componentes se irá utilizar para resolver o problema e não como deveríamos construir algo para resolver

- arquitetura:
  - ideia de algo estrutural de difícil mudança
- design:
  - relacionamento das partes internas
  - "designar": tar sentido a algo
  - equilíbrio forma x função
    - lidar com a explosão combinatória

- Edsger W. Dikstra:

> A maior causa da crise dos softwares é que as máquinas se tornaram algumas ordens de magnitude mais poderosas.
> Enquanto não tínhamos máquinas, programação não era um problemas.
> Quando tínhamos alguns poucos computadores fracos, programação se tornou um problema leve. Agora que temos computadores gigantes, programação se tornou um problema igualmente gigantesco.

- capacidade de mudança de um software está relacionada com o design

- conceito de componentização:
  - *NÃO* é o mesmo que parte
    - peças de quebra-cabeças são partes, pois sem uma delas não se completa
  - componentes deveriam ser substituíveis e padronizados
    - peças de dominós em um efeito cascata são componentes, pois cada peça pode ser substituída por outra, sem mudar o resultado final
    - podem operar cooperativamente, constituindo sistemas complexos
      - ex.: componentes eletrônicos, operam em cima de um fluxo de elétrons comum, mesmo possuindo entradas e saídas distintas
    - ficar atento aos processos de transformação de natureza
      - limita qual componente pode interagir com qual outro complemente
        - causa acoplamentos fortes


| Entrada                                               | Processamento                                                       | Saída                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------- |
| Natureza (única / múltiplas)                          | Função (transforma / cria / filtra)                                 | Natureza (única / múltiplas)                          |
| Forma (única / múltiplas ; independente / dependente) | Consistência (iguais / diferentes)                                  | Forma (única / múltiplas ; independente / dependente) |
| Generalidade (específico / geral)                     | Responsabilidade (única / múltiplas ; similares / distintas)        | Generalidade (específico / geral)                     |
| .                                                     | Robustez (código de erro / exceção / resiliente / efeito colateral) | .                                                     |

Tudo isso influência na reutilização do componente, no nível de abstração e capacidade de combinação com outros componentes.

## O código legado

É aquele que está perdendo conexão com o cotidiano, afastando as pessoas do mesmo por estar desatualizado. O que define se um código é legado ou não é seu grau de entropia.

Um código componentizado evita que tenha que se mexer no código todo.