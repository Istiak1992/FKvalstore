from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Test(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True)
    text = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return str(self.name)
