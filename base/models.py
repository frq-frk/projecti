from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
from django.db import models
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length = 30)
    deadline = models.DateField()
    done = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, null = True, blank = True)

    # def __str__(self):
    #     return self.pk

def assign_user(sender,instance,**kwargs):

    qs = Task.objects.values('user').annotate(Count('id')).order_by()
    # print(qs)
    l = list(qs)
    # print(l)
    u = min(l,key=lambda x: x['id__count'])
    k = u['user']
    user = User.objects.get(pk = k)
    # print(user)
    instance.user = user

pre_save.connect(assign_user,sender = Task)