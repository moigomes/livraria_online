from datetime import date
from decimal import Decimal

from django.db import models

class Livro(models.Model):
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano_lancamento = models.IntegerField()
    valor_emprestimo = models.DecimalField(max_digits=7, decimal_places=2)

    @staticmethod
    def get_livros_emprestados(emprestimos):
        livros_emprestados = []
        for emprestimo in emprestimos:
            quantidade_dias_emprestado = (date.today() - emprestimo.data_retirada).days
            livro = Livro.objects.filter(pk=emprestimo.livro.pk)[0]
            multa = Livro.calcular_multa(livro.valor_emprestimo, quantidade_dias_emprestado)
            juros = Livro.calcular_juros(livro.valor_emprestimo, quantidade_dias_emprestado)
            livros_emprestados.append({
                'codigo': livro.codigo,
                'titulo': livro.titulo,
                'data_retirada': emprestimo.data_retirada,
                'valor': livro.valor_emprestimo,
                'multa': multa,
                'juros': juros,
                'valor_a_pagar': livro.valor_emprestimo + juros + multa
            })

        return livros_emprestados

    @staticmethod
    def calcular_multa(valor, quantidade_dias_emprestado):

        valor_multa = 0.0

        if quantidade_dias_emprestado > 3 and quantidade_dias_emprestado <= 6:
            valor_multa = (valor / 100) * 3

        elif quantidade_dias_emprestado > 6 and quantidade_dias_emprestado <= 8:
            valor_multa =  (valor / 100) * 5

        elif quantidade_dias_emprestado > 8:
            valor_multa =  (valor / 100) * 7

        return round(Decimal(valor_multa), 2)

    @staticmethod
    def calcular_juros(valor, quantidade_dias_emprestado):

        valor_juros = 0.0

        if quantidade_dias_emprestado > 3 and quantidade_dias_emprestado <= 6:
            valor_juros = ((float(valor) / 100) * 0.2) * (quantidade_dias_emprestado - 3)

        elif quantidade_dias_emprestado > 6 and quantidade_dias_emprestado <= 8:
            valor_juros = ((float(valor) / 100) * 0.4) * (quantidade_dias_emprestado - 3)

        elif quantidade_dias_emprestado > 8:
            valor_juros = ((float(valor) / 100) * 0.6) * (quantidade_dias_emprestado - 3)

        return round(Decimal(valor_juros), 2)

    def __str__(self):
        return f'{self.titulo} - {self.codigo}'