# A essência da refatoração

- Prática e reflexão da prática.

- Identificar a relação do código com o domínio do problema. Um requisito, um bug, um conjunto de logs... de onde você extrai conhecimento, informação para criar valor necessário.

- O computador é sequencial e depende do que está na memória. Cuidado com desvios condicionais e com diversos *return* em funções. Seja o mais linear possível.

        input -> processamento -> output

- Siga um estilo. Em Python, busque seguir a PEP8. Não é estética, é legibilidade.
- Não se repita, nem se espalhe.
  - Repetição não é apenas trecho de código (sintaxe), é evitar o mesmo código com o mesmo propósito.
  - Cuidado com variáveis que se espalham em diversos pontos do código.
    - problema do *shotgun surgery*
- Nomes modelam a realidade
  - Não expresse a implementação, expresse o domínio do problema a ser resolvido
  - Expressam uma ideia, um conceito.
- Não misture tipos de dados.
- Explícito é melhor que implícito. Evite retirar o *else* de *if*, por exemplo. Isso não significa que valores *default* são errados, mas o ideal é mantê-los para casos onde há exceção.
- Avaliar balanço estética x funcionalidade.
- Menos nem sempre é mais.
  - Não sobrescreva o *input*, a menos que seja essa a finalidade da função.
- evitar *números mágicos*, deixar claro do que se trata
  - colocar como valor *default* da função facilita alteração futura, se e quando necessária.
- pensar bem se é melhor mesmo resolver algo em uma linha
- Torne evidente o que é óbvio
- Quando se percebe um conceito do funcionamento do código, tente representá-lo como um objeto (classe). Facilita perceber interações.
