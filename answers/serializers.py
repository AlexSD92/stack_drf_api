from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id', 'question', 'question_id', 'answer', 'created_at', 'updated_at'
        ]