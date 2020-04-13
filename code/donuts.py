"""
01. donuts
Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


def donuts(count):
    return f'Number of donuts: {Quantity(count)}'


class Quantity:
    def __init__(self, count, limit=10):
        self.count = count
        self.limit = limit

    @property  # permite usar um método como se fosse um atributo
    def many(self):
        return self.count >= self.limit

    def __str__(self):
        return 'many' if self.many else str(self.count)
