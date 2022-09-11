from django.db import models
from questions.models import Question
from django.contrib.auth.models import User


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False)
    answer = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.answer}"
