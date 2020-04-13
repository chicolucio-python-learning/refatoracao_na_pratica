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
    return 'Number of donuts: ' + str(Quantity(count))


class Quantity:
    def __init__(self, count, limit=10):
        self.count = count
        self.limit = limit

    def __str__(self):
        if self.count >= self.limit:
            qty = 'many'
        else:
            qty = str(self.count)

        return qty
