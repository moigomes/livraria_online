from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from emprestimos.models import Emprestimo
from livros.models import Livro


class LivroSerializer(ModelSerializer):
    situacao_livro = SerializerMethodField()

    class Meta:
        model = Livro
        fields = ['id', 'codigo', 'titulo', 'autor', 'ano_lancamento', 'valor_emprestimo', 'situacao_livro']

    def get_situacao_livro(self, obj):
        teste = Emprestimo.objects.filter(livro=obj.id).filter(data_entrega=None)
        if len(teste) > 0:
            return 'emprestado'
        return 'disponivel'
