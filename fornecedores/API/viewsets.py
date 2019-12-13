from rest_framework.viewsets import ModelViewSet
from fornecedores.models import Fornecedor
from .serializer import FornecedorSerializer

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor
    serializer_class = FornecedorSerializer
