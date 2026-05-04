from rest_framework import generics
from drf_spectacular.utils import extend_schema
from ..models.tanda import Question
from ..serializers.tanda import QuestionSerializer


@extend_schema(tags=['Tanda'])
class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
