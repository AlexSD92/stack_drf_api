from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)