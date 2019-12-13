from rest_framework.serializers import ModelSerializer
from fornecedores.models import Fornecedor

class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['cod', 'corporate_name', 'cnpj']