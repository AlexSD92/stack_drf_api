from .models import Answer
from .serializers import AnswerSerializer
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Answer.objects.all()
