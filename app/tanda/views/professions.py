from rest_framework import generics
from drf_spectacular.utils import extend_schema
from ..models.professions import Profession
from ..serializers import ProfessionSerializer


@extend_schema(tags=['Tanda'])
class ProfessionViewSet(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
