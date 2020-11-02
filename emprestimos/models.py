from django.db import models


from livros.models import Livro
from clientes.models import Cliente

class Emprestimo(models.Model):
    livro = models.OneToOneField(Livro, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    data_retirada = models.DateField()
    data_entrega = models.DateField(null=True, blank=True)
    valor_pago =  models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.livro} emprestado para {self.cliente} em {self.data_retirada}'

