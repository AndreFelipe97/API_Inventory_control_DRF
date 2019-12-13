from rest_framework.serializers import ModelSerializer
from suppliers.models import Suppliers

class SuppliersSerializer(ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ['cod', 'corporate_name', 'cnpj']