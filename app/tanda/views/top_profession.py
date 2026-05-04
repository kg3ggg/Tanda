from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from ..models import Profession
from ..serializers.professions import ProfessionSerializer
from ..serializers.top_profession import SkillScoresSerializer


@extend_schema(tags=['Tanda'])
class TopProfessionAPIView(APIView):
    @extend_schema(
        request=SkillScoresSerializer,
        responses=ProfessionSerializer(many=True),
    )
    def post(self, request):
        serializer = SkillScoresSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        skill_scores = serializer.validated_data

        # сортировка топ-3 по наибольшему значению
        sorted_skills = sorted(skill_scores.items(), key=lambda x: x[1], reverse=True)   # type: ignore
        top_3 = sorted_skills[:3]
        top_skill_names = [skill for skill, score in top_3]

        professions = Profession.objects.filter(skill__in=top_skill_names)

        result = []

        for skill_name, score in top_3:
            profession = professions.filter(skill=skill_name).first()
            if profession:
                result.append({
                    "skill": skill_name,
                    "score": score,
                    "profession": ProfessionSerializer(
                        profession, 
                        context={'request': request}  # передаём request для полного URL изображений
                    ).data
                })

        return Response(result)