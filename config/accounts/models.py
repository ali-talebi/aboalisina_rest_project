from django.db import models
from django.contrib.auth.models import User

class ActiveToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username