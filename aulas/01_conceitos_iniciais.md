# Conceitos básicos iniciais

## O que é refatorar?

*Refatorar* é melhorar a estrutura do código sem alterar seu comportamento.

- Reescrever tudo costuma ser muito mais caro do que se imagina. Reescrever tudo **não** é refatorar.

## Por quê refatorar?

- ~~Qualidade?~~ **Economia**
  - Cuidado com a armadilha da estética do código
- Melhoria no desempenho da equipe. Código mais fácil de mudar e evoluir com a necessidade do negócio.
- é um antídoto contra o envelhecimento do código
  - Identificação de *code smell*
  - recrutamento de *design patterns*
  - aplicação da refatoração
-refatoração deve sempre ser feita em código estável, que passa em testes.

## Por quê é difícil?

- abordagem errada
  - não é teórica e abstrata. É prática, um processo empírico.
- busca por regras
  - boas práticas não são regras. Cada projeto tem sua realidade, contexto e complexidade. *Na prática a teoria é outra*.
- explosão combinatória

## Quando refatorar?

- Sempre que seu código precisa acolher uma mudança.
- Deve ser uma decisão econômica, que melhora o desempenho da sua equipe.
- Priorize sempre os códigos que mudam com frequência.
- Não altere códigos que não geram ganho pra sua equipe.
- Nunca refatore um código instável. Primeiro corrija bugs.
- Otimização não é refatorar. Otimização é trabalhar com performance, benchmarks.

## Momentos da programação

- expansão: aumenta capacidade do software
- acomodação: momento para desatar nós
- consolidação: consolida as alterações para aumentos futuros

## Hipótese da resistência do design

<!-- TODO gráfico minuto 7:33 vídeo-->

Com um design ruim no começo, por não ter resistência, se entrega funcionalidades rapidamente, dando uma sensação de produtividade. No entanto, com o crescimento do projeto, se leva cada vez mais tempo para entregar resultados e pode levar ao travamento do projeto.

Com um design bom, o começo é mais lento, mas com o tempo o ritmo se mostra mais consistência, levando a uma maior confiança da equipe e dos clientes.

Gráfico complementar:

<!-- TODO gráfico minuto 10:00 -->

Programar não é apenas código, é o ambiente, o comportamento e a abordagem.

*Produtividade aumenta no estado de flow e diminui na ansiedade*