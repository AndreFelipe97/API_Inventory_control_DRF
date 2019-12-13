from rest_framework.viewsets import ModelViewSet
from suppliers.models import Suppliers
from .serializers import SuppliersSerializer

class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
