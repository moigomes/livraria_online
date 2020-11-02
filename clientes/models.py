from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
