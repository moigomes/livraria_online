from rest_framework.serializers import ModelSerializer

from emprestimos.models import Emprestimo


class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'cliente', 'livro', 'data_retirada', 'data_entrega']
