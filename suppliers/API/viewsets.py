from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from suppliers.models import Suppliers
from .serializers import SuppliersSerializer


class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = (AllowAny,)
