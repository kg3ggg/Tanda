from rest_framework import serializers
from ..models.professions import Profession

class ProfessionSerializer(serializers.ModelSerializer):
    skill_display = serializers.CharField(source='get_skill_display', read_only=True)

    class Meta:
        model = Profession
        fields = '__all__'
