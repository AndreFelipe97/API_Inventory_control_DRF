from rest_framework.viewsets import ModelViewSet
from fornecedores.models import Fornecedor
from .serializers import FornecedorSerializer

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
