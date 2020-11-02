from rest_framework.viewsets import ModelViewSet

from emprestimos.models import Emprestimo
from emprestimos.serializers import EmprestimoSerializer


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
