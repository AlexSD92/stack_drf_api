from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()