from rest_framework.viewsets import ModelViewSet

from livros.models import Livro
from livros.serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
