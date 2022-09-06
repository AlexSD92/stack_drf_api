from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'id', 'summary', 'question', 'created_at', 'updated_at'
        ]