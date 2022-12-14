from django.contrib import admin
from django.urls import path, include
from .views import logout_route


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('questions/', include('questions.urls')),
    path('answers/', include('answers.urls')),
    path('profiles/', include('profiles.urls')),
]
