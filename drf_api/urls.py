from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls')),
    path('answers/', include('answers.urls')),
    path('profiles/', include('profiles.urls')),

    path('api-auth/', include('rest_framework.urls')),
]
