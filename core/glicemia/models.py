from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Glicemia(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    value = models.BigIntegerField()
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.value} {self.user.username}'