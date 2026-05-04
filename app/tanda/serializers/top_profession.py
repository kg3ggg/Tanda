from rest_framework import serializers

class SkillScoresSerializer(serializers.Serializer):
    skill_1 = serializers.IntegerField()
    skill_2 = serializers.IntegerField()
    skill_3 = serializers.IntegerField()
    skill_4 = serializers.IntegerField()
    skill_5 = serializers.IntegerField()
    skill_6 = serializers.IntegerField()

    def validate(self, attrs):
        # преобразуем в формат skill1, skill2 и т.д.
        return {
            'skill1': attrs.get('skill_1', 0),
            'skill2': attrs.get('skill_2', 0),
            'skill3': attrs.get('skill_3', 0),
            'skill4': attrs.get('skill_4', 0),
            'skill5': attrs.get('skill_5', 0),
            'skill6': attrs.get('skill_6', 0),
        }