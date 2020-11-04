from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length = 30)
    deadline = models.DateField()
    done = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null = True, blank = True)

    # def __str__(self):
    #     return self.pk