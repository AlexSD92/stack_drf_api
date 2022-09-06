from django.urls import path
from answers import views

urlpatterns = [
    path('', views.AnswerList.as_view()),
    path('<int:pk>/', views.AnswerDetail.as_view()),
]
