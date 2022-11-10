from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Question.objects.all()
