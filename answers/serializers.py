from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Answer
        fields = [
            'id', 'question', 'question_id', 'answer', 'owner', 'created_at', 'updated_at'
        ]