from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from emprestimos.models import Emprestimo
from livros.models import Livro


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(methods=['get'], detail=True)
    def livros(self, request, pk=None):
        emprestimos = Emprestimo.objects.filter(cliente=pk)
        return Response(Livro.get_livros_emprestados(emprestimos))
