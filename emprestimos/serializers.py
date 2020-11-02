from rest_framework.serializers import ModelSerializer

from emprestimos.models import Emprestimo
from livros.serializers import LivroSerializer
from clientes.serializers import ClienteSerializer


class EmprestimoSerializer(ModelSerializer):
    livro = LivroSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Emprestimo
        fields = ['id', 'cliente', 'livro', 'data_retirada', 'data_entrega']


