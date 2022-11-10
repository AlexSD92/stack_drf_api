from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    summary = models.TextField(blank=False)
    question = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delet=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.question}"
